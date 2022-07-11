from PyQt5.QtWidgets import QLabel, QStatusBar


class GesturesStatusBar(QStatusBar):

    def __init__(self, parent):

        super().__init__(parent)
        self.activeGesturesCountLabel = QLabel()
        self.addPermanentWidget(self.activeGesturesCountLabel)
