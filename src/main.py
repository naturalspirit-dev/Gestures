""" Gestures: an application for people who loved to type

    Interface: GUI (PyQt5)
    Language: Python 3.5.2
    Created: 25 Jun 2017
    Next release date (NRD): TBD
 """

import sys
from PyQt5.QtWidgets import QApplication

APP = QApplication(sys.argv)

if __name__ == '__main__':
    from src.gui.main_window import GesturesWindow
    window = GesturesWindow()
    window.show()
    APP.exec()
