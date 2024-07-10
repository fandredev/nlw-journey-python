from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler
from uuid import uuid4 as uuid
from faker import Faker
import pytest

db_connection_handler.connect()
trip_id = str(uuid())
link_id = str(uuid())
faker = Faker()


@pytest.mark.skip(
    reason="Interactive with database, not use 'cause errors from unique constraints they can occur"
)
def test_registry_link():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "algum.com.br",
        "title": faker.sentence(),
    }

    links_repository.registry_link(links_infos)


@pytest.mark.skip(
    reason="Interactive with database, not use 'cause errors from unique constraints they can occur"
)
def test_find_links_from_trip_when_created_register_link():
    connection = db_connection_handler.get_connection()
    links_repository = LinksRepository(connection)

    links = links_repository.find_links_from_trip(trip_id)

    assert isinstance(links, list)
    assert isinstance(links[0], tuple)
