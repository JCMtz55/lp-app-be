from unittest import mock

import pytest

from src.dtos.operation_dto import OperationRequest
from src.services import operation_service


def fake_session(query):
    class FakeSession:
        def all(self):
            return [
                {"id": 1, "name": "test1", "type": "test1", "cost": 2},
                {"id": 2, "name": "test2", "type": "test2", "cost": 2}
            ]
    return FakeSession()


def test_get_operation():
    operation = operation_service.get_operation("test1")
    assert operation
    assert operation["name"] == "test1"


@pytest.mark.parametrize(
    "req,expected",
    [
        (OperationRequest({"num1": 5, "num2": 5, "type": "addition"}), 10),
        (OperationRequest({"num1": 5, "num2": 5, "type": "subtraction"}), 0),
        (OperationRequest({"num1": 5, "num2": 5, "type": "multiplication"}), 25),
        (OperationRequest({"num1": 5, "num2": 5, "type": "division"}), 1),
        (OperationRequest({"num1": 25, "type": "square_root"}), 5),
    ]
)
def test_handle_operation_success(req: OperationRequest, expected):
    res = operation_service.handle_operation(req)
    assert res == expected


def test_handle_operation_fail_when_invalid_type():
    with pytest.raises(Exception):
        operation_service.handle_operation(OperationRequest({"num1": 5, "num2": 5, "type": "raise_to_power"}))

@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (1, 2, 3),
        (5, 6, 11),
        (113, 567, 680),
    ]
)
def test_addition(num1, num2, expected):
    assert operation_service.addition(num1, num2) == expected


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (3, 2, 1),
        (11, 6, 5),
        (5, 6, -1),
    ]
)
def test_subtraction(num1, num2, expected):
    assert operation_service.subtraction(num1, num2) == expected


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (3, 2, 6),
        (11, 6, 66),
        (5, -1, -5),
    ]
)
def test_multiplication(num1, num2, expected):
    assert operation_service.multiplication(num1, num2) == expected


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        (6, 2, 3),
        (5, 10, 0.5),
        (5, -1, -5),
    ]
)
def test_division_success(num1, num2, expected):
    assert operation_service.division(num1, num2) == expected


def test_division_fails_when_division_by_zero():
    with pytest.raises(Exception):
        operation_service.division(1, 0)


@pytest.mark.parametrize(
    "num1,expected",
    [
        (25, 5),
        (44, 6.6332495807108),
        (123, 11.090536506409418),
    ]
)
def test_square_root_success(num1, expected):
    assert operation_service.square_root(num1) == expected


def test_square_root_fails_when_negative_number():
    with pytest.raises(Exception):
        operation_service.square_root(-5)


def test_random_string():
    random_str = operation_service.random_string()
    assert type(random_str) is str
    assert len(random_str) is not 0




