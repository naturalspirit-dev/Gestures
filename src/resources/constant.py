# All of the data that Gestures use will be included in here

import logging
import os
import sys
from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QT_VERSION_STR
from sip import SIP_VERSION_STR


__appname__ = 'Gestures'
__orgname__ = 'Jero Bado'
__orgdomain__ = 'jerobado.com'
__version__ = 'develop-2.0.2'
__author__ = 'Jero Bado'
KEYBOARD_VERSION = '0.13.5'     # core library that powers Gestures

APP = QApplication(sys.argv)
APP.setOrganizationName(__orgname__)
APP.setApplicationName(__appname__)

SETTINGS_GEOMETRY = f'{__appname__}_geometry'
SETTINGS_PROFILE = os.getlogin()
SETTINGS_FILENAME = f'{os.getcwd()}/{SETTINGS_PROFILE}.ini'

TEMP_HEADER = {}
class GesturesData:

    HEADERS = ['Gesture', 'Meaning']
    RECORD = []
