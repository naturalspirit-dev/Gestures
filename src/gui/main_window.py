from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget)
from PyQt5.QtCore import QSettings
from src.core.gestures import Gestures
from src.core import gestures


class GesturesUI(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gestures = Gestures()
        self.abbreviations = {}
        self._widgets()
        self._layout()
        self._properties()
        self._connections()
        self._read_settings()

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

    def _read_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        self.abbreviations = settings.value('abbreviations', self.abbreviations)
        self.reload_gestures(self.abbreviations)

    def reload_gestures(self, raw_data: dict):

        print('count -> {}'.format(len(raw_data.items())))
        for k, v in raw_data.items():
            gestures.abbreviate(k, v)
            print(k, v)

    def on_lineEdit_textChanged(self):

        self.check_fields()

    def on_addPushButton_clicked(self):

        # Get user's input
        abbv = self.abbvLineEdit.text()
        equiv = self.equivLineEdit.text()

        # Perform input validation
        if gestures.validate(abbv):
            # Register new abbreviation to keyboard
            gestures.abbreviate(abbv, equiv)

            # Store newly added abbreviations in a dictionary
            self.abbreviations[self.abbvLineEdit.text()] = self.equivLineEdit.text()

            self.display_output()   # Display output for debugging
            self.reset_gui()        # Clear QLineEdits for re-input
        else:
            print('Abbreviation already exist. Try again')

    def reset_gui(self):

        self.abbvLineEdit.setFocus()
        self.abbvLineEdit.clear()
        self.equivLineEdit.clear()

    def display_output(self):

        print('count -> {0}'.format(len(self.abbreviations)))
        for k, v in self.abbreviations.items():
            print(k, v)

    def check_fields(self) -> None:
        """ Enable or disable self.addPushButton based on LineEdit's text content. """

        if not self.abbvLineEdit.text() == '' and not self.equivLineEdit.text() == '':
            self.addPushButton.setEnabled(True)
        else:
            self.addPushButton.setEnabled(False)

    def closeEvent(self, event):

        self._write_settings()

    def _write_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        settings.setValue('abbreviations', self.abbreviations)
