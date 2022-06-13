import sqlite3
from sqlite3 import Error
from pathlib import Path
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.infrastructure.models.keyboard_gesture import KeyboardGesture as KeyboardGestureModel


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
        except Error as e:
            print(e)

        return connection

    def createTable(self):

        script_path = r'\sql\create_keyboardGestures_table.sql'
        full_path = f'{Path(__file__).parent}{script_path}'

        connection = self.createConnection()
        if connection is not None:
            try:
                with open(full_path, 'r') as file:
                    cursor = connection.cursor()
                    cursor.executescript(file.read())
            except Error as e:
                print(e)
            finally:
                connection.close()

    def addGesture(self, gesture: KeyboardGesture):

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
        cursor = connection.cursor()
        cursor.execute(sql_script, new_record)

        connection.commit()
        connection.close()

        new_gesture = KeyboardGestureModel()
        new_gesture.id = cursor.lastrowid
        new_gesture.shorthand = gesture.shorthand
        new_gesture.value = gesture.value
        new_gesture.date_created = gesture.date_created
        new_gesture.date_updated = gesture.date_updated

        return new_gesture

    def updateGesture(self, gestures_id, gesture: KeyboardGesture):

        sql_script = """
            UPDATE
                keyboardGestures
            SET
                shorthand = ?,
                value = ?
            WHERE
                id = ?
        """
        updated_record = (gesture.shorthand, gesture.value, gestures_id)

        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute(sql_script, updated_record)

        connection.commit()
        connection.close()

    def removeGesture(self, gestures_id):

        sql_script = """
            DELETE FROM keyboardGestures
            WHERE id = ?
        """

        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute(sql_script, (gestures_id,))

        connection.commit()
        connection.close()

    def getAllGestures(self):

        sql_script = """
            SELECT *
            FROM keyboardGestures
        """

        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute(sql_script)

        records = cursor.fetchall()

        return records
