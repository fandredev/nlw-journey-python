from http import HTTPStatus
from typing import Dict

from src.models.repositories.links_repository import LinksRepository


class LinkFinder:
    def __init__(self, links_repository: LinksRepository) -> None:
        self.__links_repository = links_repository

    def find(self, trip_id: str) -> Dict:
        try:
            links = self.__links_repository.find_links_from_trip(trip_id)

            formatted_links = []
            for link in links:
                formatted_links.append(
                    {"id": link[0], "link": link[2], "title": link[3]}
                )

            return {"body": {"links": formatted_links}, "status_code": HTTPStatus.OK}

        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
                "status_code": HTTPStatus.BAD_REQUEST,
            }
