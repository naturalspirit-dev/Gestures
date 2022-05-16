from PyQt5.QtWidgets import QAction
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.domain.services.keyboard_gesture_service import KeyboardGestureService
from src.gui.dialogs.add import AddGestureDialog


class NewAction(QAction):

    def __init__(self, parent):

        super().__init__('&New', parent)
        self.addGesturesDialog = AddGestureDialog()
        self.setShortcut('Ctrl+N')
        self.triggered.connect(self.showAddGestureDialog)

    def showAddGestureDialog(self):

        if self.addGesturesDialog.exec():
            # TODO: what should we do here? call the relevant service?
            _keyboardGestureService = KeyboardGestureService()

            shorthand = self.addGesturesDialog.gestureLineEdit.text()
            value = self.addGesturesDialog.valueLineEdit.text()

            keyboard_gesture = KeyboardGesture(shorthand, value)

            _keyboardGestureService.create(keyboard_gesture)


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('Ctrl+Q')
        self.triggered.connect(self.quit)

    def quit(self):

        exit(0)
