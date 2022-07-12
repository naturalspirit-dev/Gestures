from PyQt5.QtWidgets import QLabel, QStatusBar


class GesturesStatusBar(QStatusBar):

    def __init__(self, parent):

        super().__init__(parent)
        self.activeGesturesCountLabel = QLabel()
        self.addPermanentWidget(self.activeGesturesCountLabel)

    def displayMessage(self, message: str):

        self.showMessage(message, 5000)
