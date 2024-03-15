from datetime import datetime, timezone, timedelta
import pytest
from sqlalchemy import delete

from src import create_app, db
from src.models.operation_model import Operation
from src.models.record_model import Record


@pytest.fixture(scope='session')
def flask_app():
    app = create_app()

    client = app.test_client()

    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()


@pytest.fixture(scope='session')
def app_with_db(flask_app):
    db.create_all()

    yield flask_app

    db.session.commit()
    db.drop_all()


@pytest.fixture
def app_with_data(app_with_db):

    operation_add = Operation(1, "Addition", "addition", 2)
    db.session.add(operation_add)
    operation_subtract = Operation(2, "Subtraction", "subtraction", 2)
    db.session.add(operation_subtract)
    operation_multiply = Operation(3, "Multiplication", "multiplication", 4)
    db.session.add(operation_multiply)
    operation_divide = Operation(4, "Division", "division", 4)
    db.session.add(operation_divide)
    operation_squared = Operation(5, "Square Root", "square_root", 5)
    db.session.add(operation_squared)
    operation_random_string = Operation(6, "Random String", "random_string", 6)
    db.session.add(operation_random_string)

    record1 = Record(1, "test", 2, 98, "test")
    record1.created_at = datetime.now(timezone.utc) + timedelta(seconds=180)
    db.session.add(record1)

    record2 = Record(3, "test", 4, 94, "test")
    record2.created_at = datetime.now(timezone.utc) + timedelta(seconds=120)
    db.session.add(record2)

    record3 = Record(6, "test", 6, 96, "test")
    record3.created_at = datetime.now(timezone.utc) + timedelta(seconds=60)
    db.session.add(record3)

    db.session.commit()

    yield app_with_db

    db.session.execute(delete(operation_add))
    db.session.execute(delete(operation_subtract))
    db.session.execute(delete(operation_multiply))
    db.session.execute(delete(operation_divide))
    db.session.execute(delete(operation_squared))
    db.session.execute(delete(operation_random_string))

    db.session.execute(delete(record1))
    db.session.execute(delete(record2))
    db.session.execute(delete(record3))

    db.session.commit()
