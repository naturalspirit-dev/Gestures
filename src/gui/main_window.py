from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget)
from src.core.gestures import Gestures


class GesturesUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gestures = Gestures()
        self._widgets()
        self._layout()
        self._properties()
        self._connections()

    def _widgets(self):

        self.colonLabel = QLabel()
        self.abbvLineEdit = QLineEdit()
        self.equivLineEdit = QLineEdit()
        self.addPushButton = QPushButton()

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.abbvLineEdit)
        first_layer.addWidget(self.colonLabel)
        first_layer.addWidget(self.equivLineEdit)

        second_layer = QHBoxLayout()
        second_layer.addStretch()
        second_layer.addWidget(self.addPushButton)

        combine_vertically = QVBoxLayout()
        combine_vertically.addLayout(first_layer)
        combine_vertically.addLayout(second_layer)

        self.setLayout(combine_vertically)

    def _properties(self):

        self.colonLabel.setText(':')
        self.abbvLineEdit.setPlaceholderText('abbreviation')
        self.abbvLineEdit.setMaximumWidth(75)
        self.equivLineEdit.setPlaceholderText('equivalent')
        self.addPushButton.setText('&Add Gesture')
        self.addPushButton.setEnabled(False)
        self.resize(300, 71)
        self.setWindowTitle('Gestures')

    def _connections(self):

        self.abbvLineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        self.equivLineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)

    def on_lineEdit_textChanged(self):

        self.check_fields()

    def on_addPushButton_clicked(self):

        self.gestures.get_gestures(self.abbvLineEdit.text(),
                                   self.equivLineEdit.text())
        self.gestures.add_gesture_to_keyboard()
        self.gestures.show_gestures()
        self.reset_gui()

    def reset_gui(self):

        self.abbvLineEdit.setFocus()
        self.abbvLineEdit.clear()
        self.equivLineEdit.clear()

    def check_fields(self) -> None:
        """ Enable or disable self.addPushButton based on LineEdit's text content. """

        if not self.abbvLineEdit.text() == '' and not self.equivLineEdit.text() == '':
            self.addPushButton.setEnabled(True)
        else:
            self.addPushButton.setEnabled(False)
