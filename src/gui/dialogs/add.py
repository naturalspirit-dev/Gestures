# Add dialog UI

from PyQt5.QtWidgets import (QDialog,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout)
from src.gui.main_window import GesturesWindow


class AddGestureDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self):

        self.abbvLineEdit = QLineEdit()
        self.equivLineEdit = QLineEdit()
        self.okPushButton = QPushButton()

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.abbvLineEdit)
        first_layer.addWidget(self.equivLineEdit)

        second_layer = QHBoxLayout()
        second_layer.addStretch(1)
        second_layer.addWidget(self.okPushButton)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        stack_layers.addLayout(second_layer)

        self.setLayout(stack_layers)

    def _properties(self):

        self.abbvLineEdit.setPlaceholderText('abbreviation')
        self.abbvLineEdit.setMaximumWidth(75)
        self.equivLineEdit.setPlaceholderText('equivalent')
        self.okPushButton.setText('&OK')
        self.okPushButton.setEnabled(False)
        self.setWindowTitle('Add Gesture')

    def _connections(self):

        self.abbvLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.equivLineEdit.textChanged.connect(self.on_LineEdit_textChanged)
        self.okPushButton.clicked.connect(self.accept)

    def on_LineEdit_textChanged(self):

        self.check_LineEdit()

    def check_LineEdit(self) -> None:
        """ Enable or disable self.addPushButton based on LineEdit's text content. """

        if not self.abbvLineEdit.text() == '' and not self.equivLineEdit.text() == '':
            self.okPushButton.setEnabled(True)
        else:
            self.okPushButton.setEnabled(False)
