import pytest
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from uuid import uuid4 as uuid
from datetime import datetime
from faker import Faker


db_connection_handler.connect()
trip_id = str(uuid())
faker = Faker()


@pytest.mark.skip(reason="Interactive with database")
def test_create_trip():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_infos = {
        "id": trip_id,
        "destination": faker.city(),
        "start_date": datetime.strptime("03-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("08-01-2024", "%d-%m-%Y"),
        "owner_name": faker.name(),
        "owner_email": faker.email(),
    }

    trips_repository.create_trip(trips_infos)


@pytest.mark.skip(reason="Interactive with database")
def test_find_trip_by_id():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trip = trips_repository.find_trip_by_id(trip_id)

    assert trip[0] == trip_id


@pytest.mark.skip(reason="Interactive with database")
def test_update_trip_status():
    connection = db_connection_handler.get_connection()
    trips_repository = TripsRepository(connection)

    trips_repository.update_trip_status(trip_id)

    # assert trip["status"] == 1
