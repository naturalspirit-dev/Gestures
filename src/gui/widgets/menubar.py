from PyQt5.QtWidgets import QMenuBar
from src.gui.widgets.menu import FileMenu


class GesturesMenuBar(QMenuBar):

    def __init__(self, parent):

        super().__init__(parent)
        self.addMenu(FileMenu(self))
