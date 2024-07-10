from uuid import uuid4
from typing import Dict
from src.models.repositories.activities_repository import ActivitiesRepository
from http import HTTPStatus


class ActivityCreator:
    def __init__(
        self,
        activities_repository: ActivitiesRepository,
    ):
        self.__activities_repository = activities_repository

    def create(self, body, trip_id: str) -> Dict:

        try:
            id = str(uuid4())
            activities_infos = {
                "id": id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }

            self.__activities_repository.registry_activity(activities_infos)

            return {
                "body": {
                    "activity_id": id,
                },
                "status_code": HTTPStatus.CREATED,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
            }
