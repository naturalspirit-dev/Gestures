# Remove dialog UI

from PyQt5.QtWidgets import (QDialog,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout)


class RemoveGestureDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self):

        self.removeLineEdit = QLineEdit()
        self.okPushButton = QPushButton()

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.removeLineEdit)

        second_layer = QHBoxLayout()
        second_layer.addStretch(1)
        second_layer.addWidget(self.okPushButton)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        stack_layers.addLayout(second_layer)

        self.setLayout(stack_layers)

    def _properties(self):

        self.removeLineEdit.setPlaceholderText('Existing Gesture to remove')
        self.okPushButton.setText('&OK')
        self.okPushButton.setEnabled(False)
        self.resize(236, 71)
        self.setWindowTitle('Remove Gesture')

    def _connections(self):

        self.removeLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.okPushButton.clicked.connect(self.accept)

    def on_LineEdit_textChanged(self):

        self.check_LineEdit()

    def check_LineEdit(self):

        if not self.removeLineEdit.text() == '':
            self.okPushButton.setEnabled(True)
        else:
            self.okPushButton.setEnabled(False)
