import sqlite3
from sqlite3 import Error
from pathlib import Path


class GesturesDatabase:

    database_filename = 'gestures-dev.db'

    def __init__(self):

        # self.createConnection()
        self.createTable()
        self.addGesture()

    def createConnection(self):

        connection = None
        try:
            connection = sqlite3.connect(self.database_filename)
        except Error as e:
            print(e)

        return connection

    def createTable(self):

        database_connection = self.createConnection()
        script_path = r'\sql\create_keyboardGestures_table.sql'

        xx = f'{Path(__file__).parent}{script_path}'
        print(xx)

        if database_connection is not None:
            try:
                with open(xx, 'r') as file:
                    cursor = database_connection.cursor()
                    cursor.executescript(file.read())
            except Error as e:
                print(e)
            finally:
                database_connection.close()

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
