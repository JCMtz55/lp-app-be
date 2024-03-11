import uuid
import datetime

class Record:
  id: uuid
  operation_id: uuid
  user_id: uuid
  amount: int
  user_balance: int
  operation_response: str
  date: datetime

  def __init__(self, id,  operation_id, user_id, amount, user_balance, operation_response, date) -> None:
    self.id = id
    self.operation_id = operation_id
    self.user_id = user_id
    self.amount = amount
    self.user_balance = user_balance
    self.operation_response = operation_response
    self.date = date