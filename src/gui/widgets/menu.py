from PyQt5.QtWidgets import QMenu
from src.gui.widgets.action import (NewAction,
                                    QuitAction)


class FileMenu(QMenu):

    def __init__(self, parent):

        super().__init__('&File', parent)

        self.newAction = NewAction(self)
        self.quitAction = QuitAction(self)

        self.addAction(self.newAction)
        self.addAction(self.quitAction)


class HelpMenu(QMenu):

    pass


