import sys
from PyQt5.QtWidgets import QApplication
from src.gui.windows.window import GesturesMainWindow


class GesturesApplication(QApplication):

    def __init__(self):

        super().__init__(sys.argv)
        self.window = GesturesMainWindow()

    def run(self):

        self.window.show()
        self.exec()