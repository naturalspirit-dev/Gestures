from PyQt5.QtWidgets import QAction
from src.gui.dialogs.add import AddGestureDialog


class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.setShortcut('Ctrl+N')
        self.triggered.connect(self.showAddGestureDialog)

    def showAddGestureDialog(self):

        dialog = AddGestureDialog()
        if dialog.exec():
            print('add new gesture')


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('Ctrl+Q')
        self.triggered.connect(self.quit)

    def quit(self):

        exit(0)
