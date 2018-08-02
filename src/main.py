""" Gestures: an application for people who just loved to type.

    Interface: GUI (PyQt5)
    Language: Python 3.6.6
    Created: 25 Jun 2017
    Author: mokachokokarbon
 """

import sys
sys.path.append('..')
from PyQt5.QtWidgets import QApplication


APP = QApplication(sys.argv)
APP.setOrganizationName('GIPSC Core Team')
APP.setApplicationName('Gestures')

KEYPRESS_COUNT = 0


def key_listener(event):

    global KEYPRESS_COUNT
    if event.event_type == 'down':
        KEYPRESS_COUNT += 1
        print(f'[{KEYPRESS_COUNT}] key: {event.name}')


if __name__ == '__main__':
    from src.gui.main.main_ui import GesturesWindow
    window = GesturesWindow()
    window.hook_something(key_listener)
    window.show()
    APP.exec()
