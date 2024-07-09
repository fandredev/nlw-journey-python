import pytest
from .emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler
from uuid import uuid4 as uuid
from datetime import datetime, timedelta
from faker import Faker

from pytest import mark

db_connection_handler.connect()
trip_id = str(uuid())
faker = Faker()


@pytest.mark.skip(reason="Interactive with database")
def test_registry_email():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    email_infos = {
        "id": trip_id,
        "trip_id": trip_id,
        "email": faker.email(),
    }

    emails_to_invite_repository.registry_email(email_infos)


@pytest.mark.skip(reason="Interactive with database")
def test_find_emails_from_trip_when_not_created_registry_email():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    trips = emails_to_invite_repository.find_emails_from_trip(trip_id)

    assert len(trips) == 0


@pytest.mark.skip(reason="Interactive with database")
def test_find_emails_from_trip_when_created_registry_email():
    connection = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(connection)

    email_infos = {
        "id": trip_id,
        "trip_id": trip_id,
        "email": faker.email(),
    }

    emails_to_invite_repository.registry_email(email_infos)

    trips = emails_to_invite_repository.find_emails_from_trip(trip_id)

    for trip in trips:
        assert trip[0] == trip_id
        assert trip[1] == trip_id
        assert trip[2] == email_infos["email"]
