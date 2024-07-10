from sqlite3 import Connection
from typing import Dict, List, Tuple


class ParticipantsRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def registry_participants(self, participants_infos: Dict) -> None:
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
                SELECT * FROM participants WHERE trip_id = ?
            """,
            (trip_id,),
        )

        participants = cursor.fetchall()

        return participants
