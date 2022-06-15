from datetime import datetime
from PyQt5.QtWidgets import QAction
from src.domain.entities.keyboard import KeyboardGesture
from src.gui.dialogs.add import AddGestureDialog
from src.gui.dialogs.update import UpdateGestureDialog


# File Menu's action
class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.setShortcut('Ctrl+N')

    def showAddGestureDialog(self) -> KeyboardGesture:

        dialog = AddGestureDialog()
        return KeyboardGesture(shorthand=dialog.shorthandLineEdit.text(),
                               value=dialog.valueLineEdit.text(),
                               date_created=datetime.today().strftime('%x %X %p'),
                               date_updated=datetime.today().strftime('%x %X %p')) \
            if dialog.exec() else KeyboardGesture()


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('Ctrl+Q')


# Edit Menu's action
class UpdateAction(QAction):

    def __init__(self, parent):

        super().__init__('&Update', parent)

    def showUpdateGestureDialog(self, selected_index):

        shorthand = selected_index.sibling(selected_index.row(), 1)
        value = selected_index.sibling(selected_index.row(), 2)

        dialog = UpdateGestureDialog()
        dialog.shorthandLineEdit.setText(shorthand.data())
        dialog.valueLineEdit.setText(value.data())

        return KeyboardGesture(shorthand=dialog.shorthandLineEdit.text(),
                               value=dialog.valueLineEdit.text(),
                               date_updated=datetime.today().strftime('%x %X %p')) \
            if dialog.exec() else KeyboardGesture()


class DeleteAction(QAction):

    def __init__(self, parent):

        super().__init__('&Delete', parent)
