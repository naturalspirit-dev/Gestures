import sqlite3
from sqlite3 import Error
from pathlib import Path
from src.domain.entities.keyboard_gesture import KeyboardGesture


class GesturesDatabase:

    database_filename = 'gestures-dev.db'

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
            INSERT INTO keyboardGestures(shorthand, value)
            VALUES (?, ?)
        """
        new_record = (gesture.shorthand, gesture.value)

        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute(sql_script, new_record)

        connection.commit()
        connection.close()

        return cursor.lastrowid

    def updateGesture(self):

        pass

    def removeGesture(self):

        pass

    def getAllGestures(self):

        sql_script = """
            SELECT shorthand, value
            FROM keyboardGestures
        """

        connection = self.createConnection()
        cursor = connection.cursor()
        cursor.execute(sql_script)

        records = cursor.fetchall()

        return records
