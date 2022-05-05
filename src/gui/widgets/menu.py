from PyQt5.QtWidgets import QMenu
from src.gui.widgets.action import QuitAction


class FileMenu(QMenu):

    def __init__(self, parent):

        super().__init__('&File', parent)
        self.addAction(QuitAction(self))


class HelpMenu(QMenu):

    pass


