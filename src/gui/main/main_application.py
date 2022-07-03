import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from src.gui.windows.window import GesturesMainWindow
from src.gui.widgets.systemtray import GesturesSystemTray

GESTURES_VERSION = '2.0.2-beta'


class GesturesMainApplication(QApplication):

    def __init__(self):

        super().__init__(sys.argv)
        self.window = GesturesMainWindow()

        self.systemTray = GesturesSystemTray()
        self.systemTray.setToolTip(f'Gestures {GESTURES_VERSION}')

        self.systemTray.activated.connect(self.on_systemTray_activated)
        self.systemTray.systemTrayMenu.openAction.triggered.connect(self.window.show)
        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.closeAllWindows)
        self.systemTray.systemTrayMenu.quitAction.triggered.connect(self.quit)

    def on_systemTray_activated(self, reason: QSystemTrayIcon):

        if reason == QSystemTrayIcon.Trigger:
            self.window.show()

    def run(self):

        self.window.show()
        self.systemTray.show()
        self.exec()
