from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from uuid import uuid4 as uuid
from datetime import datetime, timedelta
from faker import Faker

db_connection_handler.connect()
faker = Faker()


def test_create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_infos = {
        "id": str(uuid()),
        "destination": faker.city(),
        "start_date": datetime.strptime("03-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("08-01-2024", "%d-%m-%Y"),
        "owner_name": faker.name(),
        "owner_email": faker.email(),
    }

    trips_repository.create_trip(trips_infos)
