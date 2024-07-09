from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from typing import Dict
from uuid import uuid4
from http import HTTPStatus


class TripCreator:
    def __init__(
        self,
        trip_repository: TripsRepository,
        emails_repository: EmailsToInviteRepository,
    ):
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> Dict:
        try:

            emails = body.get("emails_to_invite")

            trip_id = str(uuid4())

            # **body is a way to merge two dictionaries
            trip_infos = {**body, "id": trip_id}

            self.__trip_repository.create_trip(trip_infos)

            if emails:
                for email in emails:
                    self.__emails_repository.registry_email(
                        {"email": email, "trip_id": trip_id, "id": str(uuid4())}
                    )
            return {
                "body": {"id": trip_id},
                "status_code": HTTPStatus.CREATED,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
                "status_code": HTTPStatus.BAD_REQUEST,
            }
