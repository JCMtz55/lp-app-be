from sqlalchemy import cast, String
from src import db
from src.models.record_dto import RecordRequest
from src.models.record_model import Record
from src.services.operation_service import get_operation, handle_operation
from src.models.operation_dto import OperationRequest


def insert_record(user_id: str, operation_req: OperationRequest):
    # Get Operation
    operation = get_operation(operation_req.type)
    if operation is None:
        return 'Invalid Operation', 400
    # Get Last Record For Balance
    last_record: Record = get_user_last_record(user_id)
    current_balance = last_record.user_balance or 100
    # Validate if they can do the operation
    if current_balance > operation.cost:
        # Do operation
        operation_result = handle_operation(operation_req)
        # Save Record
        try:
            new_balance = current_balance - operation.cost
            record = Record(
                operation_id=operation.id,
                user_id=user_id,
                amount=operation.cost,
                operation_response=operation_result,
                user_balance=new_balance
            )
            db.session.add(record)
            db.session.commit()
            return record.serialize()
        except Exception as e:
            return f'Internal Server Error: {e}', 500
    return 'User balance is insufficient for this operation', 400


def get_user_last_record(user_id: str):
    last_record = (Record.query
                   .filter(Record.user_id == user_id and not Record.is_deleted)
                   .order_by(Record.created_at.desc())
                   .first()
                   )
    return last_record


def get_user_records(user_id: str, record_request: RecordRequest):
    records = []
    result = []
    if record_request.search != "":
        records = (Record.query
                   .filter(Record.user_id == user_id
                           and (cast(Record.amount, String).like(record_request.search)
                                or cast(Record.user_balance, String).like(record_request.search)
                                or cast(Record.operation_response, String).like(record_request.search)))
                   .paginate(page=record_request.page, per_page=record_request.limit))
    else:
        records = (Record.query.filter(Record.user_id == user_id).paginate(page=record_request.page,
                                                                           per_page=record_request.limit))

    for record in records.items:
        result.append(record.serialize())
    return result
