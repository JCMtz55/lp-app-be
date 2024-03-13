from datetime import datetime, timezone
from src import db


class Record(db.Model):
    __tablename__ = 'records'
    id: int = db.Column(db.Integer, primary_key=True)
    operation_id: int = db.Column(db.Integer, nullable=False)
    user_id: str = db.Column(db.String(100), nullable=False)
    amount: int = db.Column(db.Integer, nullable=False)
    user_balance: int = db.Column(db.Integer, nullable=False)
    operation_response: str = db.Column(db.String(50))
    created_at: datetime = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    is_deleted: bool = db.Column(db.Boolean, default=False)

    def __init__(self, operation_id: int, user_id: str, amount: int, user_balance: int, operation_response: str):
        self.operation_id = operation_id
        self.user_id = user_id
        self.amount = amount
        self.user_balance = user_balance
        self.operation_response = operation_response

    def serialize(self):
        return {
            "id": self.id,
            "operation_id": self.operation_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "user_balance": self.user_balance,
            "operation_response": self.operation_response,
            "created_at": self.created_at,
            "is_deleted": self.is_deleted,
        }
