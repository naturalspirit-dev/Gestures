import sqlite3
from sqlite3 import Error
from pathlib import Path
from src.domain.entities.keyboard import KeyboardGesture


class GesturesDatabase:

    database_filename = 'gestures-test.db'

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
            connection.close()

    def createConnection(self):

        connection = None
        try:
            connection = sqlite3.connect(self.database_filename)
            connection.row_factory = sqlite3.Row
        except Error as e:
            print(e)

        return connection

    def createTable(self):

        script_path = r'\sql\create_keyboardGestures_table.sql'
        full_path = f'{Path(__file__).parent}{script_path}'

        connection = self.createConnection()
        with connection:
            with open(full_path, 'r') as file:
                connection.executescript(file.read())

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
            SELECT *
            FROM keyboardGestures
        """

        connection = self.createConnection()
        with connection:
            records = connection.execute(sql_script).fetchall()
            return [KeyboardGesture(id=record['id'],
                                    shorthand=record['shorthand'],
                                    value=record['value'],
                                    date_created=record['date_created'],
                                    date_updated=record['date_updated']) for record in records]
