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


def key_listener(event):

    if event.event_type == 'down':
        print(f'key: {event.name}')


if __name__ == '__main__':
    # [x] TODO: remove try...except, left alt bug already solved
    from src.gui.main.main_ui import GesturesWindow
    window = GesturesWindow()
    window.hook_something(key_listener)
    window.show()
    APP.exec()
