# Initiating spin! ~Cooper, Interstellar, 2014

import os
import platform
import sys
from src.gui.dialogs.messageboxes import DDayMessageBox

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: <%(funcName)s> %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
    
from src.resources.constant import __version__

def welcome_message() -> None:

    message = """
    Gestures, an application for people who just love to type.
    
    Created: 25 Jun 2017
    Author: Jero Bado <tokidokitalkyou@gmail.com>
    """
    print(message)


def platform_check() -> None:
    """ Identify the application's current environment. """

    logging.info(f'User -> {os.getlogin()}')
    logging.info(f'Machine -> {platform.machine()}')
    logging.info(f'Platform -> {platform.platform()}')
    logging.info(f'System -> {platform.system()}')


def dependency_check() -> None:
    """ Check tools version for debugging. """

    from PyQt5.QtCore import QT_VERSION_STR
    from PyQt5.Qt import PYQT_VERSION_STR
    from sip import SIP_VERSION_STR
    from src.resources.constant import (__version__,
                                        KEYBOARD_VERSION)
    from gui.main.main_application import GESTURES_VERSION

    logging.info(f'Gestures version -> {GESTURES_VERSION}')
    logging.info(f'Python version -> {sys.version[:5]}')
    logging.info(f'PyQt version -> {PYQT_VERSION_STR}')
    logging.info(f'keyboard version -> {KEYBOARD_VERSION}')
    logging.info(f'Qt version -> {QT_VERSION_STR}')
    logging.info(f'SIP version -> {SIP_VERSION_STR}')


def valid_license() -> bool:
    """ Check if license expired. """

    # [] TODO: What is the best way to limit its usage?
    return False


if valid_license():   # Gestures' end of usage
    dialog = DDayMessageBox
    if dialog.exec():
        sys.exit(0)
else:
    welcome_message()
    platform_check()
    dependency_check()
    # then start executing main.py...
