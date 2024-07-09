from sqlite3 import Connection
from typing import Dict, Tuple


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

    def find_trip_by_id(self, trip_id: str) -> Tuple:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                SELECT * FROM trips WHERE id = ?
            """,
            (trip_id,),
        )

        # Fetchone() returns the next row of a query result set, returning a single sequence, or None when no more data is available.
        trip = cursor.fetchone()

        return trip

    def update_trip_status(self, trip_id: str) -> None:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                UPDATE trips SET status = 1 WHERE id = ?
            """,
            (trip_id,),
        )

        self.__connection_database.commit()
