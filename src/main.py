""" Gestures: an application for people who just loved to type.

    Interface: GUI (PyQt5)
    Language: Python 3.6.3
    Created: 25 Jun 2017
    Author: mokachokokarbon
 """

import sys
from PyQt5.QtWidgets import QApplication

sys.path.append('..')

APP = QApplication(sys.argv)
APP.setOrganizationName('GIPSC Core Team')
APP.setApplicationName('Gestures')


# TEST: adding a method to 'listen' to any key pressed to catch an existing value error
def key_listener(event):

    try:
        if event.event_type == 'down':
            print(f'key: {event.name}')

    except ValueError as e:
        print(f'ValueError catched! last known key: {event.name} \n Type: {type(e)} - {e}')

    except Exception as e:
        print(f'An error has occurred, last known key: {event.name} \n Type: {type(e)} - {e}')


if __name__ == '__main__':
    from src.gui.main_window import GesturesWindow
    window = GesturesWindow()
    window.hook_something(key_listener)  # if this thing does not catch the error, wrap this if block in try...except
    window.show()
    APP.exec()
