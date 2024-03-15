from src import db
from enum import StrEnum


class Operation(db.Model):
    __tablename__ = 'operations'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(50), nullable=False)
    type: str = db.Column(db.String(50), nullable=False)
    cost: int = db.Column(db.Integer, nullable=False)

    def __init__(self, id: int, name: str, type: str, cost: int):
        self.id = id
        self.name = name
        self.type = type
        self.cost = cost

    @classmethod
    def valid_type(cls, type: str):
        try:
            OperationType(type)
        except ValueError:
            raise Exception("Invalid operation type")
        return True

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "cost": self.cost
        }


class OperationType(StrEnum):
    ADDITION = "addition",
    SUBTRACTION = "subtraction",
    MULTIPLICATION = "multiplication",
    DIVISION = "division",
    SQUARE_ROOT = "square_root",
    RANDOM_STRING = "random_string",
