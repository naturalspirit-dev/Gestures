""" Gestures: an application for people who just loved to type.

    Interface: GUI (PyQt5)
    Language: Python 3.6.6
    Created: 25 Jun 2017
    Author: mokachokokarbon
 """

import logging
import sys
sys.path.append('..')
from src.gui.main.main_application import GesturesMainApplication

KEYPRESS_COUNT = 0


def configure_app_icon() -> None:
    """ This will show the icon of Gestures in the taskbar. """

    import ctypes
    APP_ID = u'mokachokokarbon.jerobado.gesture.2-0'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)


def key_listener(event):

    global KEYPRESS_COUNT
    if event.event_type == 'down':
        KEYPRESS_COUNT += 1
        logging.info(f'#{KEYPRESS_COUNT} key: {event.name}')


if __name__ == '__main__':

    configure_app_icon()
    app = GesturesMainApplication()
    app.run()
