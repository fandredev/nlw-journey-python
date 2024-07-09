import sqlite3


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"  # Path to the database file
        self.__connection = None

    def connect(self) -> None:
        # check_same_thread=False is used to allow the connection to be used in multiple threads
        connection = sqlite3.connect(self.__connection_string, check_same_thread=False)

        self.__connection = connection

    def get_connection(self) -> sqlite3.Connection:
        return self.__connection


db_connection_handler = DbConnectionHandler()
