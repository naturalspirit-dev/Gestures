import sys
from PyQt5.QtWidgets import QApplication
from src.gui.windows.window import GesturesMainWindow
from src.gui.widgets.systemtray import GesturesSystemTray

GESTURES_VERSION = '2.0.2-beta'


class GesturesMainApplication(QApplication):

    def __init__(self):

        super().__init__(sys.argv)
        self.window = GesturesMainWindow()
        self.systemTray = GesturesSystemTray()

        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.closeAllWindows)
        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.quit)

    def run(self):

        self.window.show()
        self.systemTray.show()
        self.exec()
