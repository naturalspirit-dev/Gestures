from datetime import datetime
from PyQt5.QtWidgets import QAction
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.gui.dialogs.add import AddGestureDialog
from src.gui.dialogs.update import UpdateGestureDialog


# File Menu's action
class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.addGesturesDialog = AddGestureDialog
        self.keyboardGesture = KeyboardGesture
        self.setShortcut('Ctrl+N')
        self.triggered.connect(self.showAddGestureDialog)

    def showAddGestureDialog(self):

        self.addGesturesDialog = AddGestureDialog()
        self.keyboardGesture = KeyboardGesture()
        if self.addGesturesDialog.exec():
            self.addGesturesDialog.shorthand = self.addGesturesDialog.gestureLineEdit.text()
            self.addGesturesDialog.value = self.addGesturesDialog.valueLineEdit.text()
            self.keyboardGesture = KeyboardGesture(self.addGesturesDialog.shorthand,
                                                   self.addGesturesDialog.value)
            self.keyboardGesture.date_created = datetime.today().strftime('%x %X %p')
            self.keyboardGesture.date_updated = datetime.today().strftime('%x %X %p')


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('Ctrl+Q')


# Edit Menu's action
class UpdateAction(QAction):

    def __init__(self, parent):

        super().__init__('&Update', parent)
        self.updateGestureDialog = UpdateGestureDialog
        self.keyboardGesture = KeyboardGesture

    def showUpdateGestureDialog(self, selected_index):

        self.updateGestureDialog = UpdateGestureDialog()
        gesture = selected_index.sibling(selected_index.row(), 1)
        value = selected_index.sibling(selected_index.row(), 2)
        self.updateGestureDialog.gestureLineEdit.setText(gesture.data())
        self.updateGestureDialog.valueLineEdit.setText(value.data())
        self.keyboardGesture = KeyboardGesture()

        if self.updateGestureDialog.exec():
            self.updateGestureDialog.shorthand = self.updateGestureDialog.gestureLineEdit.text()
            self.updateGestureDialog.value = self.updateGestureDialog.valueLineEdit.text()
            self.keyboardGesture = KeyboardGesture(self.updateGestureDialog.shorthand,
                                                   self.updateGestureDialog.value)
            self.keyboardGesture.date_updated = datetime.today().strftime('%x %X %p')


class DeleteAction(QAction):

    def __init__(self, parent):

        super().__init__('&Delete', parent)
