from PyQt5.QtWidgets import QMenu
from src.gui.widgets.action import (NewAction,
                                    QuitAction)


class FileMenu(QMenu):

    def __init__(self, parent):

        super().__init__('&File', parent)
        self.addAction(NewAction(self))
        self.addAction(QuitAction(self))


class HelpMenu(QMenu):

    pass


