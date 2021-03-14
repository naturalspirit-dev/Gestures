# All of the data that Gestures use will be included in here

import os
import sys
from PyQt5.QtWidgets import QApplication


__appname__ = 'Gestures'
APP = QApplication(sys.argv)
APP.setOrganizationName(__org__)
APP.setApplicationName(__appname__)

TEMP_HEADER = {}

SETTINGS_GEOMETRY = f'{__appname__}_geometry'
SETTINGS_PROFILE = f'{__appname__}_{os.getlogin()}-test-profile'

class GesturesData:

    HEADERS = ['Gesture', 'Meaning']
    RECORD = []
