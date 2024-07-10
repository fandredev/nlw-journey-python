from src.models.repositories.participants_repository import ParticipantsRepository
from typing import Dict
from http import HTTPStatus


class ParticipantFinder:
    def __init__(self, participant_repository: ParticipantsRepository):
        self.__participant_repository = participant_repository

    def find_participants_from_trip(self, trip_id: str) -> Dict:
        try:
            participants = self.__participant_repository.find_participants_from_trip(
                trip_id
            )

            participants_infos = []

            for participant in participants:
                participants_infos.append(
                    {
                        "id": participant[0],
                        "name": participant[1],
                        "is_confirmed": participant[2],
                        "email": participant[3],
                    }
                )

            return {
                "body": {"participants": participants_infos},
                "status_code": HTTPStatus.OK,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
                "status_code": HTTPStatus.BAD_REQUEST,
            }
