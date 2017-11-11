from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QInputDialog,
                             QListView)
from PyQt5.QtCore import (QSettings,
                          Qt)
from src.core.gestures import KeyboardGesture


# [x] TODO: create add.py for the 'Add' dialog
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

        self.gesturesListView = QListView()
        self.addPushButton = QPushButton()
        self.updatePushButton = QPushButton()
        self.removePushButton = QPushButton()

    def _layout(self):

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.addPushButton)
        button_layout.addWidget(self.updatePushButton)
        button_layout.addWidget(self.removePushButton)
        button_layout.addStretch(1)

        first_layer = QHBoxLayout()
        first_layer.addWidget(self.gesturesListView)
        first_layer.addLayout(button_layout)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        self.setLayout(stack_layers)

    def _properties(self):

        self.addPushButton.setText('&Add')
        self.updatePushButton.setText('&Update')
        self.removePushButton.setText('&Remove')
        self.resize(445, 222)   # width, height
        self.setWindowTitle('Gestures')

    def _connections(self):

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

    def on_addPushButton_clicked(self):

        try:
            from src.gui.dialogs.add import AddGestureDialog
            dialog = AddGestureDialog()
            if dialog.exec():
                # Get user's input
                abbv = dialog.abbvLineEdit.text()
                equiv = dialog.equivLineEdit.text()

                # Register new abbreviation to keyboard
                self.gesture.add_gesture(abbv, equiv)

                # Store newly added abbreviations in a dictionary
                self.abbreviations[abbv] = equiv
                self.display_output()   # Display output for debugging

        except ValueError:
            # [] TODO: add a message box to display the message below
            print(f'Abbreviation already exist. Try again.')

        except Exception as e:
            print(f'Gestures: {type(e)}{e}.')

    def on_updatePushButton_clicked(self):
        """ Event handler that update an existing gesture. """

        try:
            from src.gui.dialogs.update import UpdateGestureDialog
            dialog = UpdateGestureDialog(self)
            if dialog.exec():
                try:
                    # get input
                    current_abbv = dialog.current_abbvLineEdit.text()
                    current_equiv = dialog.current_equivLineEdit.text()
                    new_abbv = dialog.new_abbvLineEdit.text()
                    new_equiv = dialog.new_equivLineEdit.text()

                    # remove current gesture
                    del self.abbreviations[current_abbv]
                    self.gesture.remove_gesture(current_abbv)

                    # add new gesture
                    self.gesture.update_gesture(new_abbv, new_equiv)
                    self.abbreviations[new_abbv] = new_equiv

                    # report what happend
                    self.display_output()

                except ValueError as e:
                    print(f'{e}')

        except Exception as e:
            print(e)

    # [] TODO: create 'Remove' dialog
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

        print('\ncount -> {0}'.format(len(self.abbreviations)))
        for k, v in self.abbreviations.items():
            print(k, v)

    def closeEvent(self, event):

        self._write_settings()

    def _write_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        settings.setValue('abbreviations', self.abbreviations)

    def resizeEvent(self, event):

        #print(f'{self.width()} x {self.height()}')
        pass
