from PyQt5.QtWidgets import QAction
from src.gui.dialogs.add import AddGestureDialog


class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.addGesturesDialog = AddGestureDialog
        self.setShortcut('Ctrl+N')
        self.triggered.connect(self.showAddGestureDialog)

    def showAddGestureDialog(self):

        self.addGesturesDialog = AddGestureDialog()
        if self.addGesturesDialog.exec():
            self.addGesturesDialog.shorthand = self.addGesturesDialog.gestureLineEdit.text()
            self.addGesturesDialog.value = self.addGesturesDialog.valueLineEdit.text()


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('Ctrl+Q')
