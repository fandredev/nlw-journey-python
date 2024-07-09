from sqlite3 import Connection
from typing import Dict


class TripsRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def create_trip(self, trips_infos: Dict) -> None:
        # The cursor is used to interact with the database
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                INSERT INTO trips (id, destination, start_date, end_date, owner_name, owner_email)
                values (?, ?, ?, ?, ?, ?)
            """,
            (
                trips_infos["id"],
                trips_infos["destination"],
                trips_infos["start_date"],
                trips_infos["end_date"],
                trips_infos["owner_name"],
                trips_infos["owner_email"],
            ),
        )

        # Commit the transaction
        self.__connection_database.commit()
