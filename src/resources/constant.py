# All of the data that Gestures use will be included in here

import os

__appname__ = 'Gestures'
__org__ = 'GIPSC Core Team'
__version__ = '1.4'
__author__ = 'mokachokokarbon'
KEYBOARD_VERSION = '0.13.2'     # core library that powers Gestures

TEMP_HEADER = {}

SETTINGS_GEOMETRY = f'{__appname__}_geometry'
SETTINGS_PROFILE = f'{__appname__}_{os.getlogin()}-test-profile'

class GesturesData:

    HEADERS = ['Gesture', 'Meaning']
    RECORD = []
