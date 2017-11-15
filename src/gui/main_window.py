from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QTableView)
from PyQt5.QtCore import (QSettings,
                          Qt)
from src.core.gestures import KeyboardGesture
from src.gui.dialogs.messageboxes import (AddMessageBox,
                                          UpdateMessageBox,
                                          RemoveMessageBox)
from src.resources.constant import (RECORD,
                                    TEMP_HEADER)
from src.resources.models import GestureTableModel


class GesturesWindow(QWidget):
    """ Gestures' main user interface. """

    def __init__(self, parent=None):

        super().__init__(parent)
        self.gesture = KeyboardGesture()
        self.abbreviations = {}
        self.data_before_editing = ''
        self._widgets()
        self._layout()
        self._properties()
        self._connections()
        self._read_settings()

    def _widgets(self):

        self.gesturesTableView = QTableView()
        self.gesturesTableModel = GestureTableModel()
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
        first_layer.addWidget(self.gesturesTableView)
        first_layer.addLayout(button_layout)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(first_layer)
        self.setLayout(stack_layers)

    def _properties(self):

        self.gesturesTableView.setModel(self.gesturesTableModel)
        self.addPushButton.setText('&Add')
        self.updatePushButton.setText('&Update')
        self.removePushButton.setText('&Remove')
        self.resize(445, 222)   # width, height
        self.setWindowTitle('Gestures')

    def _connections(self):

        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)
        self.updatePushButton.clicked.connect(self.on_updatePushButton_clicked)
        self.removePushButton.clicked.connect(self.on_removePushButton_clicked)
        self.gesturesTableView.doubleClicked.connect(self.on_gesturesTableView_activated)
        self.gesturesTableModel.dataChanged.connect(self.on_something_happen)

    def on_gesturesTableView_activated(self):

        index = self.gesturesTableView.currentIndex()
        self.data_before_editing = index.data()
        #print(f'current data {self.data_before_editing}')

    # [] TODO: you need to deep work the update button
    def on_something_happen(self):

        index = self.gesturesTableView.currentIndex()
        row = index.row()
        col = index.column()
        new_data = index.data()
        #print(f'on_something_happen: dataChanged? {row, col, new_data}')
        #print(f'on_something_happen: RECORD {RECORD}')
        #print(f'{self.abbreviations}')
        print(f'previous_data: {self.data_before_editing}, new_data: {new_data}')
        # Get key of edited data -> this will update only the 'equivalent'
        for k, v in self.abbreviations.items():
            if self.data_before_editing in (k, v):
                print(f'your key is {k}')
                break



    def _read_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        self.abbreviations = settings.value('abbreviations', self.abbreviations)
        self.reload_gestures(self.abbreviations)

    def reload_gestures(self, raw_data: dict):

        print('count -> {}'.format(len(raw_data.items())))
        for k, v in raw_data.items():
            self.gesture.add_gesture(k, v)
            print(k, v)
            self.update_gesture_tableview(k, v)

    def update_gesture_tableview(self, gesture, equivalent):
        """ Insert one row at a time in the GestureTableView. """

        # TEST: Displaying to the TableView
        TEMP_HEADER['gesture'] = gesture
        TEMP_HEADER['equivalent'] = equivalent
        RECORD.append(list(TEMP_HEADER.values()))
        self.gesturesTableModel.insertRows(len(RECORD), 1)
        self.gesturesTableView.setModel(self.gesturesTableModel)

    def on_addPushButton_clicked(self):

        try:
            from src.gui.dialogs.add import AddGestureDialog
            dialog = AddGestureDialog(self)
            if dialog.exec():
                # Get user's input
                abbv = dialog.abbvLineEdit.text()
                equiv = dialog.equivLineEdit.text()

                # Register new abbreviation to keyboard
                self.gesture.add_gesture(abbv, equiv)

                # Store newly added abbreviations in a dictionary
                self.abbreviations[abbv] = equiv
                self.display_output()   # Display output for debugging

                self.update_gesture_tableview(abbv, equiv)

        except ValueError:
            print(f'\'{abbv}\' already exist. Try again.')
            AddMessageBox.setText(f'\'{abbv}\' already exist. Try again.')
            AddMessageBox.show()

    def on_updatePushButton_clicked(self):
        """ Event handler that update an existing gesture. """

        try:
            from src.gui.dialogs.update import UpdateGestureDialog
            dialog = UpdateGestureDialog(self)

            if dialog.exec():
                # Get input
                new_abbv = dialog.new_abbvLineEdit.text()
                new_equiv = dialog.new_equivLineEdit.text()

                # Remove current gesture
                self.gesture.remove_gesture(new_abbv)
                del self.abbreviations[new_abbv]

                # Add new gesture
                self.gesture.add_gesture(new_abbv, new_equiv)
                self.abbreviations[new_abbv] = new_equiv

                # Report what happend
                self.display_output()

        except ValueError:
            print(f'No existing gesture found for \'{new_abbv}\'. Try again.')
            UpdateMessageBox.setText(f'No existing gesture found for \'{new_abbv}\'. Try again.')
            UpdateMessageBox.show()

    def on_removePushButton_clicked(self):
        """ Display an input dialog that will accept a gesture to remove. """

        try:
            from src.gui.dialogs.remove import RemoveGestureDialog
            dialog = RemoveGestureDialog(self)

            if dialog.exec():
                # Get user input
                gesture_to_remove = dialog.removeLineEdit.text()

                # Remove gesture
                self.gesture.remove_gesture(gesture_to_remove)           # raise ValueError when this fails
                del self.abbreviations[gesture_to_remove]                # remove internal list of gestures

                self.display_output()

                # Clear the Gesture TableView first
                self.gesturesTableModel.removeRows(0, len(RECORD))
                self.gesturesTableView.setModel(self.gesturesTableModel)
                RECORD.clear()

                # Start re-inserting the updated gestures
                for gesture, equivalent in self.abbreviations.items():
                    self.update_gesture_tableview(gesture, equivalent)

        except ValueError:
            print(f'No existing gesture found for \'{gesture_to_remove}\'. Try again.')
            RemoveMessageBox.setText(f'No existing gesture found for \'{gesture_to_remove}\'. Try again.')
            RemoveMessageBox.show()

    def display_output(self):
        """ Display output in the command line. For debugging purposes. """

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
