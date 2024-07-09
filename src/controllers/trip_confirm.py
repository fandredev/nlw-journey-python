from typing import Dict
from src.models.repositories.trips_repository import TripsRepository
from http import HTTPStatus


class TripConfirm:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def confirm(self, trip_id: str) -> Dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)

            return {
                "body": {"message": "Trip confirmed successfully", "trip_id": trip_id},
                "status_code": HTTPStatus.NO_CONTENT,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
            }
