from src.models.repositories.trips_repository import TripsRepository

from typing import Dict
from http import HTTPStatus


class TripFinder:
    def __init__(self, trips_repository: TripsRepository) -> None:
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id: str):

        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("Trip not found")

            return {
                "body": {
                    "trip": {
                        "id": trip[0],
                        "destination": trip[1],
                        "starts_at": trip[2],
                        "ends_at": trip[3],
                        "status": trip[6],
                    }
                },
                "status_code": HTTPStatus.OK,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
                "status_code": HTTPStatus.BAD_REQUEST,
            }
