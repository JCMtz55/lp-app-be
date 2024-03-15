import datetime

from src import db
from src.models.record_model import Record
from src.services.operation_service import get_operation, handle_operation
from src.dtos.operation_dto import OperationRequest
from sqlalchemy import false


def insert_record(user_id: str, operation_req: OperationRequest):
    # Get Operation
    operation = get_operation(operation_req.type)
    if operation is None:
        return 'Invalid Operation', 400
    # Get Last Record For Balance
    last_record: Record = get_user_last_record(user_id)
    current_balance = getattr(last_record, 'user_balance', 100)
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
                user_balance=new_balance,
                created_at=datetime.datetime.now()
            )
            db.session.add(record)
            db.session.commit()
            return record.serialize()
        except Exception as e:
            return f'Internal Server Error: {e}', 500
    raise Exception('User balance is insufficient for this operation', 400)


def get_user_last_record(user_id: str):
    last_record = (Record.query
                   .filter(Record.user_id == user_id and Record.is_deleted == false())
                   .order_by(Record.created_at.desc())
                   .first()
                   )
    return last_record


def get_user_records(user_id: str):
    result = []
    records = Record.query.filter(Record.user_id == user_id).all()
    for record in records:
        if not record.is_deleted:
            result.append(record.serialize())
    return result


def delete_user_record(record_id: int):
    try:
        # Get Record to Delete
        record_to_delete = Record.query.filter(Record.id == record_id).first()
        record_to_delete.is_deleted = True
        db.session.commit()
        return True
    except Exception as e:
        return f'Internal Server Error: {e}', 500


def refund_user_record(user_id: str, record_id: int):
    try:
        # Get Record to Delete
        record_to_refund = Record.query.filter(Record.id == record_id).first()
        # Get Last Record
        last_record = get_user_last_record(user_id)
        # Create New Record with refund
        new_balance = last_record.user_balance + record_to_refund.amount
        new_record = Record(
            operation_id=record_to_refund.operation_id,
            user_id=user_id,
            amount=(record_to_refund.amount * -1),
            operation_response=record_to_refund.operation_response,
            user_balance=new_balance,
            created_at=datetime.datetime.now()
        )
        db.session.add(new_record)
        db.session.commit()
        return new_record.serialize()
    except Exception as e:
        return f'Internal Server Error: {e}', 500
