import json
import os
import logging
from typing import Final

DATABASE_NAME: Final[str] = 'database.json'


def load_json_database(path: str) -> dict:
    """
    Load a json database from a file.
    """
    logging.debug('Loading database from %s', path)
    with open(path, 'r') as f:
        return json.load(f)


class Database:
    """
    A database of paths.
    """
    def __init__(self) -> None:
        # if the database file doesn't exist, create it
        if not os.path.isfile(DATABASE_NAME):
            self.database = {}
            with open(DATABASE_NAME, 'w') as f:
                json.dump(self.database, f)
        else:
            self.database = load_json_database(DATABASE_NAME)

    def contains(self, path: str) -> bool:
        logging.debug('Checking if %s is in database', path)
        return path in self.database

    def add(self, path: str) -> None:
        logging.debug('Adding %s to database', path)
        self.database[path] = True
        with open(DATABASE_NAME, 'w') as f:
            json.dump(self.database, f)
