""" Gestures: an application for people who just loved to type

    Interface: GUI (PyQt5)
    Language: Python 3.6.3
    Created: 25 Jun 2017
 """

import sys
from PyQt5.QtWidgets import QApplication

sys.path.append('..')
APP = QApplication(sys.argv)

if __name__ == '__main__':
    from src.gui.main_window import GesturesWindow
    window = GesturesWindow()
    window.show()
    APP.exec()
