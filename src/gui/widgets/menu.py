from PyQt5.QtWidgets import QMenu
from src.gui.widgets.action import (NewAction,
                                    UpdateAction,
                                    DeleteAction,
                                    OpenGesturesAction,
                                    QuitAction)


class FileMenu(QMenu):

    def __init__(self, parent):

        super().__init__('&File', parent)
        self.newAction = NewAction(self)
        self.quitAction = QuitAction(self)

        self.addAction(self.newAction)
        self.addAction(self.quitAction)


class EditMenu(QMenu):

    def __init__(self, parent):

        super().__init__('&Edit', parent)
        self.updateAction = UpdateAction(self)
        self.deleteAction = DeleteAction(self)

        self.addAction(self.updateAction)
        self.addAction(self.deleteAction)


class HelpMenu(QMenu):

    pass


class SystemTrayMenu(QMenu):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.quitAction = QuitAction(self)
        self.openAction = OpenGesturesAction(self)

        self.addAction(self.openAction)
        self.addSeparator()
        self.addAction(self.quitAction)
