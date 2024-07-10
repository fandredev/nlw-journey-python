from sqlite3 import Connection
from typing import Dict, List, Tuple


class ParticipantsRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def registry_participant(self, participants_infos: Dict) -> None:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                INSERT INTO participants (id, trip_id, emails_to_invite_id, name)
                values (?, ?, ?, ?)
            """,
            (
                participants_infos["id"],
                participants_infos["trip_id"],
                participants_infos["emails_to_invite_id"],
                participants_infos["name"],
            ),
        )

        self.__connection_database.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                SELECT p.id, p.name, p.is_confirmed, e.email 
                FROM participants as p 
                JOIN emails_to_invite as e 
                ON e.id = p.emails_to_invite_id
                WHERE p.trip_id = ?
            """,
            (trip_id,),
        )

        participants = cursor.fetchall()

        return participants

    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                UPDATE participants 
                SET is_confirmed = 1
                WHERE id = ?
            """,
            (participant_id,),
        )

        self.__connection_database.commit()
