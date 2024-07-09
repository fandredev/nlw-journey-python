from sqlite3 import Connection
from typing import Dict, List, Tuple


class EmailsToInviteRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def registry_email(self, email_infos: Dict) -> None:
        # The cursor is used to interact with the database
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                INSERT INTO emails_to_invite (id, trip_id, email)
                values (?, ?, ?)
            """,
            (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"],
            ),
        )

        # Commit the transaction
        self.__connection_database.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                SELECT * FROM emails_to_invite WHERE trip_id = ?
            """,
            (trip_id,),
        )

        # Fetchone() returns the next row of a query result set, returning a single sequence, or None when no more data is available.
        trips = cursor.fetchall()

        return trips
