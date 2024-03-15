import requests
from math import sqrt
from src.models.operation_model import Operation, OperationType
from src.dtos.operation_dto import OperationRequest


def get_operation(operation_type: str):
    operation = Operation.query.filter_by(type=operation_type).first()
    return operation


def get_operations():
    result = []
    operations = Operation.query.all()
    for operation in operations:
        result.append(operation.serialize())
    return result


def handle_operation(operation_req: OperationRequest):
    res = 0
    if Operation.valid_type(operation_req.type):
        match operation_req.type:
            case OperationType.ADDITION:
                res = addition(operation_req.num1, operation_req.num2)
            case OperationType.SUBTRACTION:
                res = subtraction(operation_req.num1, operation_req.num2)
            case OperationType.MULTIPLICATION:
                res = multiplication(operation_req.num1, operation_req.num2)
            case OperationType.DIVISION:
                res = division(operation_req.num1, operation_req.num2)
            case OperationType.SQUARE_ROOT:
                res = square_root(operation_req.num1)
            case OperationType.RANDOM_STRING:
                res = random_string()
    return res


def addition(num1: int, num2: int):
    return num1 + num2


def subtraction(num1: int, num2: int):
    return num1 - num2


def multiplication(num1: int, num2: int):
    return num1 * num2


def division(num1: int, num2: int):
    try:
        val = num1 / num2
        return val
    except:
        raise Exception(f'Cannot divide by 0', 500)


def square_root(num: int):
    try:
        val = sqrt(num)
        return val
    except:
        raise Exception('Cannot calculate square root of a negative number', 500)


def random_string():
    try:
        r = requests.get('https://www.random.org/strings/?num=1&len=10&digits=on&loweralpha=on&unique=off&format=plain&rnd=new')
        return r.text.strip()
    except Exception as e:
        raise Exception(f'There was an error on requesting random string: {e}', 500)
