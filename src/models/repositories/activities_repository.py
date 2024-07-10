from sqlite3 import Connection
from typing import Dict, List, Tuple


class ActivitiesRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def registry_activity(self, activities_infos: Dict) -> None:
        # The cursor is used to interact with the database
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                INSERT INTO activities (id, trip_id, title, occurs_at)
                values (?, ?, ?, ?)
            """,
            (
                activities_infos["id"],
                activities_infos["trip_id"],
                activities_infos["title"],
                activities_infos["occurs_at"],
            ),
        )

        # Commit the transaction
        self.__connection_database.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                SELECT * FROM activities WHERE trip_id = ?
            """,
            (trip_id,),
        )

        # Fetchone() returns the next row of a query result set, returning a single sequence, or None when no more data is available.
        activities = cursor.fetchall()

        return activities
