from datetime import datetime
from PyQt5.QtWidgets import QAction
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.gui.dialogs.add import AddGestureDialog
from src.gui.dialogs.update import UpdateGestureDialog


# File Menu's action
class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.setShortcut('Ctrl+N')

    def showAddGestureDialog(self) -> KeyboardGesture:

        dialog = AddGestureDialog()
        new_gesture = KeyboardGesture()
        if dialog.exec():
            return KeyboardGesture(shorthand=dialog.gestureLineEdit.text(),
                                   value=dialog.valueLineEdit.text(),
                                   date_created=datetime.today().strftime('%x %X %p'),
                                   date_updated=datetime.today().strftime('%x %X %p'))
        return new_gesture


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
            self.keyboardGesture = KeyboardGesture(shorthand=self.updateGestureDialog.shorthand,
                                                   value=self.updateGestureDialog.value,
                                                   date_updated=datetime.today().strftime('%x %X %p'))


class DeleteAction(QAction):

    def __init__(self, parent):

        super().__init__('&Delete', parent)
