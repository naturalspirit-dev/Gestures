# Initiating spin! ~Cooper, Interstellar, 2014

import sys
from src.gui.dialogs.messageboxes import DDayMessageBox


def perform_dependency_check() -> None:
    """ Check tools version for debugging. """

    import logging
    from PyQt5.QtCore import QT_VERSION_STR
    from PyQt5.Qt import PYQT_VERSION_STR
    from sip import SIP_VERSION_STR
    from src.resources.constant import (__version__,
                                        KEYBOARD_VERSION)

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(f'[GESTURES]: Gestures version {__version__}')
    logging.info(f'[GESTURES]: Python version {sys.version[:5]}')
    logging.info(f'[GESTURES]: PyQt version {PYQT_VERSION_STR}')
    logging.info(f'[GESTURES]: keyboard version {KEYBOARD_VERSION}')
    logging.info(f'[GESTURES]: Qt version {QT_VERSION_STR}')
    logging.info(f'[GESTURES]: SIP version {SIP_VERSION_STR}')


def valid_license() -> bool:
    """ Check if license expired. """

    # [] TODO: What is the best way to limit its usage?
    return False


if valid_license():   # Gestures' end of usage
    dialog = DDayMessageBox
    if dialog.exec():
        sys.exit(0)
else:
    perform_dependency_check()
    # then start executing main.py...
