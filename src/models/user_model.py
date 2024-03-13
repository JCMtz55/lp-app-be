from src import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    cognito_id: str = db.Column(db.String(100), nullable=False)
    username: str = db.Column(db.String(100), nullable=False, unique=True)
    status: bool = db.Column(db.Boolean(), nullable=False)