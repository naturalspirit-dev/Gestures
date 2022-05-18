# Main User Interface of the 'Add' dialog

from PyQt5.QtWidgets import (QDialog,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout)


class AddGestureDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.shorthand = ''
        self.value = ''
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self):

        self.newLabel = QLabel()
        self.gestureLineEdit = QLineEdit()
        self.valueLineEdit = QLineEdit()
        self.okPushButton = QPushButton()

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.newLabel)

        second_layer = QHBoxLayout()
        second_layer.addWidget(self.gestureLineEdit)
        second_layer.addWidget(self.valueLineEdit)

        third_layer = QHBoxLayout()
        third_layer.addStretch(1)
        third_layer.addWidget(self.okPushButton)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        stack_layers.addLayout(second_layer)
        stack_layers.addLayout(third_layer)

        self.setLayout(stack_layers)

    def _properties(self):

        self.newLabel.setText('Add new Gesture:')
        self.gestureLineEdit.setPlaceholderText('Gesture')
        self.gestureLineEdit.setMaximumWidth(75)
        self.valueLineEdit.setPlaceholderText('Value')
        self.okPushButton.setText('&OK')
        self.okPushButton.setEnabled(False)
        self.setWindowTitle('Add Gesture')
        self.resize(310, 71)

    def _connections(self):

        self.gestureLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.valueLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.okPushButton.clicked.connect(self.accept)

    def on_LineEdit_textChanged(self):

        self.check_LineEdit()

    def check_LineEdit(self) -> None:
        """ Enable or disable self.addPushButton based on QLineEdit's text content. """

        if not self.gestureLineEdit.text() == '' and not self.valueLineEdit.text() == '':
            self.okPushButton.setEnabled(True)
        else:
            self.okPushButton.setEnabled(False)
