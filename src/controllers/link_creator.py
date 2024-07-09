from src.models.repositories.links_repository import LinksRepository

from typing import Dict
from http import HTTPStatus

from uuid import uuid4


class LinkCreator:
    def __init__(self, link_repository: LinksRepository) -> None:
        self.__link_repository = link_repository

    def create(self, body, trip_id: str) -> Dict:
        try:
            link_id = str(uuid4())
            link_infos = {
                "id": link_id,
                "link": body["link"],
                "title": body["title"],
                "trip_id": trip_id,
            }

            self.__link_repository.registry_link(link_infos)

            return {
                "body": {
                    "link_id": link_id,
                },
                "status_code": HTTPStatus.CREATED,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST}
            }
