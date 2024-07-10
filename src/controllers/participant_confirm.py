from typing import Dict
from src.models.repositories.participants_repository import ParticipantsRepository
from http import HTTPStatus


class ParticipantConfirm:
    def __init__(self, participants_repository: ParticipantsRepository) -> None:
        self.__participants_repository = participants_repository

    def confirm(self, participant_id: str) -> Dict:
        try:
            self.__participants_repository.update_participant_status(participant_id)

            return {
                "body": {
                    "message": "Trip confirmed successfully",
                    "trip_id": participant_id,
                },
                "status_code": HTTPStatus.NO_CONTENT,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
            }
