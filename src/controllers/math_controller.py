from flask import request, Response, jsonify, Blueprint
from src.services.operation_service import addition, substraction, multiplication, division, square_root;
from src.models.operation_model import Operation, OperationType
from src.models.operation_dto import OperationRequest

# math controller blueprint to be registered with api blueprint
math = Blueprint("math", __name__)


# route for operation
@math.route('/', methods=["POST"])
def handle_operation():
    data = request.get_json()
    operation_req = OperationRequest(data)
    res = 0
    if operation_req is not None and Operation.valid_type(operation_req.type):

        # Get User Credits
        # Call operator
        match operation_req.type:
            case OperationType.ADDITION:
                res = addition(operation_req.num1, operation_req.num2)
            case OperationType.SUBSTRACTION:
                res = substraction(operation_req.num1, operation_req.num2)
            case OperationType.MULTIPLICATION:
                res = multiplication(operation_req.num1, operation_req.num2)
            case OperationType.DIVISION:
                res = division(operation_req.num1, operation_req.num2)
            case OperationType.SQUARE_ROOT:
                res = square_root(operation_req.num1)

    return jsonify(res), 201
