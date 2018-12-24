""" Gestures: an application for people who just loved to type.

    Interface: GUI (PyQt5)
    Language: Python 3.6.6      # [] TODO: can you upgrade to 3.7.x?
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


def configure_app_icon() -> None:
    """ This will show the icon of Gestures in the taskbar. """

    import ctypes
    APP_ID = u'novus.jerobado.gesture.1-2'      # [] TODO: update version here
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


def key_listener(event):

    global KEYPRESS_COUNT
    if event.event_type == 'down':
        KEYPRESS_COUNT += 1
        print(f'[{KEYPRESS_COUNT}] key: {event.name}')


if __name__ == '__main__':
    from src.gui.main.main_ui import GesturesWindow
    configure_app_icon()
    window = GesturesWindow()
    window.hook_something(key_listener)
    window.show()
    APP.exec()
