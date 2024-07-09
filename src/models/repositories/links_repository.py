from sqlite3 import Connection
from typing import Dict, List, Tuple


class LinksRepository:
    def __init__(self, connection_database: Connection) -> None:
        self.__connection_database = connection_database

    def registry_link(self, link_infos: Dict) -> None:
        # The cursor is used to interact with the database
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                INSERT INTO links (id, trip_id, link, title)
                values (?, ?, ?, ?)
            """,
            (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            ),
        )

        # Commit the transaction
        self.__connection_database.commit()

    def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__connection_database.cursor()

        cursor.execute(
            """
                SELECT * FROM links WHERE trip_id = ?
            """,
            (trip_id,),
        )

        # Fetchone() returns the next row of a query result set, returning a single sequence, or None when no more data is available.
        links = cursor.fetchall()

        return links
