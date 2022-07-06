from PyQt5.QtWidgets import QMenuBar
from src.gui.widgets.menu import (FileMenu,
                                  EditMenu,
                                  HelpMenu)


class GesturesMenuBar(QMenuBar):

    def __init__(self, parent):

        super().__init__(parent)
        self.fileMenu = FileMenu(self)
        self.editMenu = EditMenu(self)
        self.helpMenu = HelpMenu(self)

        self.addMenu(self.fileMenu)
        self.addMenu(self.editMenu)
        self.addMenu(self.helpMenu)
