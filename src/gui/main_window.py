from PyQt5.QtWidgets import (QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QTableView,
                             QHeaderView)
from PyQt5.QtCore import (QSettings,
                          Qt,
                          QItemSelectionModel)
from src.core.gestures import KeyboardGesture
from src.gui.dialogs.messageboxes import (AddMessageBox,
                                          UpdateMessageBox,
                                          RemoveMessageBox)
from src.resources.constant import (TEMP_HEADER,
                                    GesturesData)
from src.resources.models import GestureTableModel

RECORD = GesturesData.RECORD


class GesturesWindow(QWidget):
    """ Gestures' main user interface. """

    def __init__(self, parent=None):

        super().__init__(parent)
        self.keyboardGesture = KeyboardGesture()
        self.abbreviations = {}
        self.selectedData = ''
        self._widgets()
        self._layout()
        self._properties()
        self._connections()
        self._read_settings()

    def _widgets(self):

        self.gesturesTableView = QTableView()
        #self.gesturesHeaderView = QHeaderView()
        self.gesturesItemSelectionModel = QItemSelectionModel()
        self.gesturesTableModel = GestureTableModel()
        self.countLabel = QLabel()
        self.addPushButton = QPushButton()
        self.updatePushButton = QPushButton()
        self.removePushButton = QPushButton()

    def _layout(self):

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.addPushButton)
        right_layout.addWidget(self.updatePushButton)
        right_layout.addWidget(self.removePushButton)
        right_layout.addStretch(1)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.gesturesTableView)
        left_layout.addWidget(self.countLabel)

        combine_layout = QHBoxLayout()
        combine_layout.addLayout(left_layout)
        combine_layout.addLayout(right_layout)
        self.setLayout(combine_layout)

    def _properties(self):

        self.gesturesTableView.setModel(self.gesturesTableModel)
        horizontalHeaderView = self.gesturesTableView.horizontalHeader()
        horizontalHeaderView.setStretchLastSection(True)
        self.gesturesItemSelectionModel.setModel(self.gesturesTableModel)
        self.gesturesTableView.setSelectionModel(self.gesturesItemSelectionModel)
        self.addPushButton.setText('&Add')
        self.updatePushButton.setText('&Update')
        self.removePushButton.setText('&Remove')
        self.resize(445, 222)   # width, height
        self.setWindowTitle('Gestures')

    def _connections(self):

        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)
        self.updatePushButton.clicked.connect(self.on_updatePushButton_clicked)
        self.removePushButton.clicked.connect(self.on_removePushButton_clicked)

        # When the user interacts with the table using the tab or arrow keys
        self.gesturesTableView.activated.connect(self.updateSelectedData)
        self.gesturesTableView.clicked.connect(self.updateSelectedData)
        self.gesturesTableView.doubleClicked.connect(self.updateSelectedData)
        self.gesturesItemSelectionModel.selectionChanged.connect(self.updateSelectedData)

        # When the user edit a cell in the table
        self.gesturesTableModel.dataChanged.connect(self.on_gesturesTableModel_dataChanged)

    def updateSelectedData(self):

        index = self.gesturesTableView.currentIndex()
        self.selectedData = index.data()

    def on_gesturesTableModel_dataChanged(self):

        index = self.gesturesTableView.currentIndex()
        new_data = index.data()

        # Get key of edited data -> this will update only the 'equivalent'
        for gesture, meaning in self.abbreviations.items():
            if self.selectedData in (gesture, meaning):
                # remove current keyboardGesture
                self.keyboardGesture.remove_gesture(gesture)
                del self.abbreviations[gesture]

                # Add new keyboardGesture
                # check if data to be edited is the key
                if self.selectedData == gesture:
                    self.keyboardGesture.add_gesture(new_data, meaning)
                    self.abbreviations[new_data] = meaning
                else:
                    self.keyboardGesture.add_gesture(gesture, new_data)
                    self.abbreviations[gesture] = new_data

                # Report what happend
                self.display_output()
                break

    def _read_settings(self):

        settings = QSettings('GIPSC Core Team', 'Gestures')
        self.abbreviations = settings.value('abbreviations', self.abbreviations)
        self.reload_gestures(self.abbreviations)

    def reload_gestures(self, raw_data: dict):

        active_gestures = len(raw_data)
        self.countLabel.setText(f'Active: {active_gestures}')
        print(f'Active: {active_gestures}')
        for k, v in raw_data.items():
            self.keyboardGesture.add_gesture(k, v)
            print(k, v)
            self.update_gesture_tableview(k, v)

    def update_gesture_tableview(self, gesture, equivalent):
        """ Insert one row at a time in the GestureTableView. """

        # TEST: Displaying to the TableView
        TEMP_HEADER['gesture'] = gesture
        TEMP_HEADER['meaning'] = equivalent
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
                self.keyboardGesture.add_gesture(abbv, equiv)

                # Store newly added abbreviations in a dictionary
                self.abbreviations[abbv] = equiv
                self.display_output()   # Display output for debugging

                self.update_gesture_tableview(abbv, equiv)

        except ValueError:
            print(f'\'{abbv}\' already exist. Try again.')
            AddMessageBox.setText(f'\'{abbv}\' already exist. Try again.')
            AddMessageBox.show()

    def on_updatePushButton_clicked(self):
        """ Event handler that update an existing keyboardGesture. """

        try:
            from src.gui.dialogs.update import UpdateGestureDialog
            dialog = UpdateGestureDialog(self)

            if dialog.exec():
                # Get input
                new_abbv = dialog.new_abbvLineEdit.text()
                new_equiv = dialog.new_equivLineEdit.text()

                # Remove current keyboardGesture
                self.keyboardGesture.remove_gesture(new_abbv)

                # Add new keyboardGesture
                self.keyboardGesture.add_gesture(new_abbv, new_equiv)
                self.abbreviations[new_abbv] = new_equiv

                # Report what happend
                self.display_output()

                # Clear the Gesture TableView first
                self.gesturesTableModel.removeRows(0, len(RECORD))
                self.gesturesTableView.setModel(self.gesturesTableModel)
                RECORD.clear()

                # Start re-inserting the updated gestures
                for gesture, equivalent in self.abbreviations.items():
                    self.update_gesture_tableview(gesture, equivalent)

        except ValueError:
            print(f'No existing gesture found for \'{new_abbv}\'. Try again.')
            UpdateMessageBox.setText(f'No existing gesture found for \'{new_abbv}\'. Try again.')
            UpdateMessageBox.show()

    def on_removePushButton_clicked(self):
        """ Display an input dialog that will accept a keyboardGesture to remove. """

        try:
            from src.gui.dialogs.remove import RemoveGestureDialog
            dialog = RemoveGestureDialog(self)

            if dialog.exec():
                # Get user input
                gesture_to_remove = dialog.removeLineEdit.text()

                # Remove keyboardGesture
                self.keyboardGesture.remove_gesture(gesture_to_remove)  # raise ValueError when this fails
                del self.abbreviations[gesture_to_remove]               # remove internal list of gestures

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

        active_gestures = len(self.abbreviations)
        self.countLabel.setText(f'Active: {active_gestures}')
        print(f'\nActive: {active_gestures}')
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
