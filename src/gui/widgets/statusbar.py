from PyQt5.QtWidgets import QLabel, QStatusBar
from src.domain.services import keyboardGestureService


class GesturesStatusBar(QStatusBar):

    def __init__(self, parent):

        super().__init__(parent)
        self.activeGesturesCountLabel = QLabel()
        self.addPermanentWidget(self.activeGesturesCountLabel)

        records = keyboardGestureService.getTotalRecords()
        self.activeGesturesCountLabel.setText(f'Active: {records}')

    def displayMessage(self, message: str):

        self.showMessage(message, 5000)
