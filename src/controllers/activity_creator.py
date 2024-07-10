from uuid import uuid4
from typing import Dict
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from http import HTTPStatus


class ParticipantCreator:
    def __init__(
        self,
        participant_repository: ParticipantsRepository,
        emails_to_invite_repository: EmailsToInviteRepository,
    ):
        self.__participant_repository = participant_repository
        self.__emails_to_invite_repository = emails_to_invite_repository

    def create(self, body, trip_id: str) -> Dict:

        try:
            participant_id = str(uuid4())
            email_id = str(uuid4())

            emails_infos = {
                "email": body["email"],
                "id": email_id,
                "trip_id": trip_id,
            }

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }

            self.__emails_to_invite_repository.registry_email(emails_infos)
            self.__participant_repository.registry_participant(participant_infos)

            return {
                "body": {
                    "participant_id": participant_id,
                },
                "status": HTTPStatus.CREATED,
            }
        except Exception as exception:
            return {
                "body": {"message": str(exception), "error": HTTPStatus.BAD_REQUEST},
            }
