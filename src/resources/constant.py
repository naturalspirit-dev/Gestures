# All of the data that Gestures use will be included in here

import logging
import os
import sys
from PyQt5.QtWidgets import QApplication


__appname__ = 'Gestures'
__org__ = 'Moka, Choko, Karbon'
__version__ = 'develop-1.4.1'
__author__ = 'Jero Bado'
KEYBOARD_VERSION = '0.13.5'     # core library that powers Gestures

APP = QApplication(sys.argv)
APP.setOrganizationName(__org__)
APP.setApplicationName(__appname__)

SETTINGS_GEOMETRY = f'{__appname__}_geometry'
SETTINGS_PROFILE = os.getlogin()
SETTINGS_FILENAME = f'../{SETTINGS_PROFILE}.ini'

TEMP_HEADER = {}
class GesturesData:

    HEADERS = ['Gesture', 'Meaning']
    RECORD = []
