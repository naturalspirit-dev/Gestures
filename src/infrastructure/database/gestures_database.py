import sqlite3
from sqlite3 import Error
from typing import Optional

from src.domain.entities.keyboard import KeyboardGesture


class GesturesDatabase:

    database_filename = 'gestures-dev.db'
    # database_filename = 'gestures-test.db'  # for UAT

    def __init__(self):

        self.createDatabase()
        self.createTable()

    def createDatabase(self):

        connection = None
        try:
            connection = sqlite3.connect(self.database_filename)
        except Error as e:
            print(e)
        finally:
            if connection:
                connection.close()

    def createConnection(self):

        connection = None
        try:
            connection = sqlite3.connect(self.database_filename)
            connection.row_factory = sqlite3.Row
            return connection
        except Error as e:
            print(e)

        return connection

    def createTable(self):

        sql_script = """
            CREATE TABLE IF NOT EXISTS keyboardGestures(
                id INTEGER PRIMARY KEY,
                shorthand TEXT NOT NULL,
                value TEXT NO NULL,
                date_created TEXT NO NULL,
                date_updated TEXT NO NULL
)        """

        connection = self.createConnection()
        with connection:
            connection.execute(sql_script)

        connection.close()

    def addGesture(self, gesture: KeyboardGesture) -> KeyboardGesture:

        sql_script = """
            INSERT INTO keyboardGestures(shorthand, value, date_created, date_updated)
            VALUES (?, ?, ?, ?)
        """
        new_record = (
            gesture.shorthand,
            gesture.value,
            gesture.date_created,
            gesture.date_updated
        )

        connection = self.createConnection()
        with connection:
            gesture.id = connection.execute(sql_script, new_record).lastrowid

        connection.close()
        return gesture

    def updateGesture(self, gesture: KeyboardGesture):

        sql_script = """
            UPDATE
                keyboardGestures
            SET
                shorthand = ?,
                value = ?,
                date_created = ?,
                date_updated = ?
            WHERE
                id = ?
        """
        updated_record = (
            gesture.shorthand,
            gesture.value,
            gesture.date_created,
            gesture.date_updated,
            gesture.id
        )

        connection = self.createConnection()
        with connection:
            connection.execute(sql_script, updated_record)

        connection.close()

    def removeGesture(self, gesture: KeyboardGesture):

        sql_script = """
            DELETE FROM keyboardGestures
            WHERE id = ?
        """

        connection = self.createConnection()
        with connection:
            connection.execute(sql_script, (gesture.id,))

        connection.close()

    def getAllGestures(self) -> list[KeyboardGesture]:

        sql_script = """
            SELECT * FROM keyboardGestures
        """

        connection = self.createConnection()
        with connection:
            records = connection.execute(sql_script).fetchall()
            return [KeyboardGesture(id=record['id'],
                                    shorthand=record['shorthand'],
                                    value=record['value'],
                                    date_created=record['date_created'],
                                    date_updated=record['date_updated']) for record in records]

    def getGestureByShorthand(self, gesture: KeyboardGesture) -> Optional[KeyboardGesture]:

        sql_script = """
            SELECT * FROM keyboardGestures
            WHERE shorthand = ?
        """

        connection = self.createConnection()
        with connection:
            record = connection.execute(sql_script, (gesture.shorthand,)).fetchone()
            if record:
                return KeyboardGesture(id=record['id'],
                                       shorthand=record['shorthand'],
                                       value=record['value'],
                                       date_created=record['date_created'],
                                       date_updated=record['date_updated'])
            else:
                return None
