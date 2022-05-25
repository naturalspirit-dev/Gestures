# Main User Interface of the 'Update' dialog

from PyQt5.QtWidgets import (QDialog,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout)


class UpdateGestureDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.shorthand = ''
        self.value = ''
        self.selectedRecord = None
        self._widgets()
        self._properties()
        self._layout()
        self._connections()

    def _widgets(self):

        self.existingLabel = QLabel()
        self.gestureLineEdit = QLineEdit()
        self.valueLineEdit = QLineEdit()
        self.okPushButton = QPushButton()

    def _properties(self):

        self.existingLabel.setText('Existing Gesture to update:')
        self.gestureLineEdit.setPlaceholderText('Gesture')
        self.gestureLineEdit.setMaximumWidth(75)
        self.valueLineEdit.setPlaceholderText('Meaning')
        self.okPushButton.setText('&OK')
        self.okPushButton.setEnabled(False)
        self.setWindowTitle('Update Gesture')
        self.resize(310, 71)

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.existingLabel)

        second_layer = QHBoxLayout()
        second_layer.addWidget(self.gestureLineEdit)
        second_layer.addWidget(self.valueLineEdit)

        third_layer = QHBoxLayout()
        third_layer.addStretch()
        third_layer.addWidget(self.okPushButton)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        stack_layers.addLayout(second_layer)
        stack_layers.addLayout(third_layer)

        self.setLayout(stack_layers)

    def _connections(self):

        self.gestureLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.valueLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.okPushButton.clicked.connect(self.accept)

    def on_LineEdit_textChanged(self):

        self.check_LineEdit()

    def check_LineEdit(self) -> None:
        """ Enable or disable self.addPushButton based on LineEdit's text content. """

        if not self.gestureLineEdit.text() == '' and not self.valueLineEdit.text() == '':
            self.okPushButton.setEnabled(True)
        else:
            self.okPushButton.setEnabled(False)
