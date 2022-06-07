import sqlite3
from sqlite3 import Error
from pathlib import Path


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

    def addGesture(self):

        sql_script = """
            INSERT INTO keyboardGestures(shorthand, value)
            VALUES ('second', 'second record')
        """

        database_connection = self.createConnection()
        cursor = database_connection.cursor()
        cursor.execute(sql_script)
        database_connection.commit()
        database_connection.close()

    def updateGesture(self):

        pass

    def removeGesture(self):

        pass
