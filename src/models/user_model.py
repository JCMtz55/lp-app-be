
import uuid

class User:
  id: uuid
  name: str
  password: str
  status: bool


  def __init__(self, id, name, password, status) -> None:
   self.id = id
   self.name = name
   self.password = password
   self.status = status


