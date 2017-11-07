from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QInputDialog)
from PyQt5.QtCore import (QSettings,
                          Qt)
from src.core.gestures import KeyboardGesture


class GesturesWindow(QWidget):
    """ Gestures' main user interface. """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gesture = KeyboardGesture()
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
        self.updatePushButton = QPushButton()
        self.removePushButton = QPushButton()

    def _layout(self):

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.abbvLineEdit)
        first_layer.addWidget(self.colonLabel)
        first_layer.addWidget(self.equivLineEdit)

        second_layer = QHBoxLayout()
        second_layer.addStretch()
        second_layer.addWidget(self.addPushButton)
        second_layer.addWidget(self.updatePushButton)
        second_layer.addWidget(self.removePushButton)

        combine_vertically = QVBoxLayout()
        combine_vertically.addLayout(first_layer)
        combine_vertically.addLayout(second_layer)

        self.setLayout(combine_vertically)

    def _properties(self):

        self.colonLabel.setText(':')
        self.abbvLineEdit.setPlaceholderText('abbreviation')
        self.abbvLineEdit.setMaximumWidth(75)
        self.equivLineEdit.setPlaceholderText('equivalent')
        self.addPushButton.setText('&Add')
        self.addPushButton.setEnabled(False)
        self.updatePushButton.setText('&Update')
        self.removePushButton.setText('&Remove')
        self.resize(300, 71)
        self.setWindowTitle('Gestures')

    def _connections(self):

        self.abbvLineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        self.equivLineEdit.textChanged.connect(self.on_lineEdit_textChanged)
        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)
        self.updatePushButton.clicked.connect(self.on_updatePushButton_clicked)
        self.removePushButton.clicked.connect(self.on_removePushButton_clicked)

    def _read_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        self.abbreviations = settings.value('abbreviations', self.abbreviations)
        self.reload_gestures(self.abbreviations)

    def reload_gestures(self, raw_data: dict):

        print('count -> {}'.format(len(raw_data.items())))
        for k, v in raw_data.items():
            self.gesture.add_gesture(k, v)
            print(k, v)

    def on_lineEdit_textChanged(self):

        self.check_fields()
        self.abbreviations.update()

    def on_addPushButton_clicked(self):

        try:
            # Get user's input
            abbv = self.abbvLineEdit.text()
            equiv = self.equivLineEdit.text()

            # Register new abbreviation to keyboard
            self.gesture.add_gesture(abbv, equiv)

            # Store newly added abbreviations in a dictionary
            self.abbreviations[abbv] = equiv
            self.display_output()   # Display output for debugging
            self.reset_gui()        # Clear QLineEdits for re-input

        except ValueError:
            print(f'Abbreviation already exist. Try again.')

        except Exception as e:
            print(f'Gestures: {type(e)}{e}.')

    def reset_gui(self):

        self.abbvLineEdit.setFocus()
        self.abbvLineEdit.clear()
        self.equivLineEdit.clear()

    def on_updatePushButton_clicked(self):
        """ Event handler that update an existing gesture. """

        # [] TODO: make this happen
        # GUI design:
        #   > dialog with the list of all existing gestures
        # get existing gesture to update: abbv, equiv
        # get new gesture
        # check if existing
        # if not, perform updating of gesture
        # else, try again
        try:
            from src.gui.dialogs.update import UpdateGestureDialog

            dialog = UpdateGestureDialog(self)
            if dialog.exec():
                print('update!!')

        except Exception as e:
            print(e)

    def on_removePushButton_clicked(self):
        """ Display an input dialog that will accept a gesture to remove. """

        try:
            user_input = QInputDialog.getText(self, 'Remove Gesture', 'Gesture to remove:', QLineEdit.Normal)
            user_gesture = user_input[0]
            if not user_gesture == '':
                del self.abbreviations[user_gesture]                # remove first internal list of gestures
                self.gesture.remove_gesture(user_gesture)           # perform removal of gesture
                print(f'[GES]: \'{user_gesture}\' now removed.')    # display result
                self.display_output()
        except Exception as e:  # KeyError: no gesture found
            print(e)

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
