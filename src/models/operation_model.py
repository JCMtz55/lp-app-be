import uuid
from enum import StrEnum

class Operation:
  id: uuid
  type: str
  cost: int
  
  def __init__(self, id, type, cost) -> None:
    self.id = id
    self.type = type
    self.cost = cost

  @classmethod
  def valid_type(cls, type: str):
    try:
        OperationType(type)
    except ValueError:
        raise Exception("Invalid operation type")
    return True
    

class OperationType(StrEnum):
  ADDITION = "addition",
  SUBSTRACTION = "subtraction",
  MULTIPLICATION = "multiplication",
  DIVISION = "division",
  SQUARE_ROOT = "square_root",
  RANDOM_STRING = "random_string",

