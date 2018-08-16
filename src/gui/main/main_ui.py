# Main User Interface of Gestures

import keyboard as kb
import webbrowser as wb
from PyQt5.QtWidgets import (QLabel,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QTableView)
from PyQt5.QtCore import (QSettings,
                          QItemSelectionModel,
                          QSortFilterProxyModel,
                          Qt)
from src.core.gestures import KeyboardGesture
from src.gui.dialogs.messageboxes import (AddMessageBox,
                                          UpdateMessageBox,
                                          RemoveMessageBox)
from src.gui.widgets.tableview import GesturesTableView
from src.resources.constant import (__appname__,
                                    GesturesData,
                                    SETTINGS_GEOMETRY,
                                    TEMP_HEADER)
from src.resources.models import GestureTableModel

RECORD = GesturesData.RECORD


# [] TODO: last column does not stretch after using the Add, Update and Remove button
class GesturesWindow(QWidget):
    """ Gestures' main user interface. """

    def __init__(self, parent=None):

        super().__init__(parent)
        self.keyboardGesture = KeyboardGesture()
        self.settings = QSettings()
        self.gestures = {}      # This will hold all the existing gestures
        self._widgets()
        self._layout()
        self._read_settings()
        self._properties()
        self._connections()
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY, self.saveGeometry()))

    def _widgets(self):

        # self.gesturesTableView = QTableView()
        self.gesturesTableView = GesturesTableView()
        self.gesturesItemSelectionModel = QItemSelectionModel()
        self.gesturesTableModel = GestureTableModel()
        self.gesturesSortFilterProxyModel = QSortFilterProxyModel()
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

        # create first the main model

        # feed filterModel with main model
        self.gesturesSortFilterProxyModel.setSourceModel(self.gesturesTableModel)

        self.gesturesTableView.setModel(self.gesturesSortFilterProxyModel)
        self.gesturesTableView.setAlternatingRowColors(True)
        self.gesturesTableView.setSortingEnabled(True)
        self.gesturesTableView.sortByColumn(0, Qt.AscendingOrder)
        self.gesturesTableView.setShowGrid(False)

        #self.gesturesItemSelectionModel.setModel(self.gesturesTableModel)
        #self.gesturesTableView.horizontalHeader().setStretchLastSection(True)
        #self.gesturesTableView.setSelectionModel(self.gesturesItemSelectionModel)
        self.addPushButton.setText('&Add')
        self.updatePushButton.setText('&Update')
        self.removePushButton.setText('&Remove')
        self.resize(409, 364)   # width, height
        self.setWindowTitle(__appname__)

    def _connections(self):

        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)
        self.updatePushButton.clicked.connect(self.on_updatePushButton_clicked)
        self.removePushButton.clicked.connect(self.on_removePushButton_clicked)

        # When the user interacts with the table using the tab or arrow keys
        self.gesturesTableView.activated.connect(self.update_selectedData)
        self.gesturesTableView.clicked.connect(self.update_selectedData)
        self.gesturesTableView.doubleClicked.connect(self.update_selectedData)
        self.gesturesItemSelectionModel.selectionChanged.connect(self.update_selectedData)

        # When the user edit a cell in the table
        self.gesturesTableModel.dataChanged.connect(self.on_gesturesTableModel_dataChanged)

    def update_selectedData(self):

        # self.selectedData = self.gesturesTableView.currentIndex().data()
        # print(f'row: {row}x col: {col} -> new_data: {new_data}')
        index = self.gesturesTableView.currentIndex()
        row = index.row()
        col = index.column()
        # self.selectedData = index.data()
        self.selectedData = self.gesturesTableView.current_data
        # print(f'row x col: {row} x {col} -> previous_data: {self.selectedData}')
        print(f'update_selectedData -> {self.gesturesTableView.current_data} x {self.gesturesTableView.previous_data}')

    def update_settings(self):
        """ Update gestures dict for every add, update and delete. """

        self.settings.setValue('abbreviations', self.gestures)

    def on_gesturesTableModel_dataChanged(self):

        # [] TODO: whew! you solve the problem at last! so far updating directly in the TableView is good without any error.
        # Beautify the code when you come back from vacation.
        index = self.gesturesTableView.currentIndex()
        row = index.row()
        col = index.column()
        new_data = index.data()
        self.selectedData = self.gesturesTableView.current_data     # This solve your freaking problem so far
        print(f'on_dataChanged: new data -> {new_data}\n\tselected data -> {self.selectedData}')
        # print(f'on_dataChanged: new data -> {new_data}\n\tselected data -> {self.gesturesTableView.current_data}')

        try:
            # Check first if the new_data is an existing gesture
            if new_data in self.gestures.keys():
                RECORD[row][col] = self.selectedData
                raise ValueError

            print(f'selectedData before for loop: {self.selectedData}')
            # Get key of edited data -> this will update only the 'meaning'
            for gesture, meaning in self.gestures.items():

                if self.selectedData in (gesture, meaning):
                    print(f'"{self.selectedData}" found in ({gesture}, {meaning})')
                    # Remove current keyboardGesture
                    self.keyboardGesture.remove_gesture(gesture)
                    print(f'deleting {self.gestures[gesture]}')
                    del self.gestures[gesture]

                    # Add new keyboardGesture
                    # check if data to be edited is the key
                    if self.selectedData == gesture:
                        self.determine_gesture(new_data, meaning)
                        self.gestures[new_data] = meaning
                        print('your editing a key')
                    else:
                        self.determine_gesture(gesture, new_data)
                        self.gestures[gesture] = new_data
                        print('your editing a meaning')

                    self.update_settings()
                    self.display_output()
                    break
                else:
                    print(f'{self.selectedData} not found in self.gestures')

        except ValueError:
            print(f'\'{new_data}\' already exist. Try again.')
            UpdateMessageBox.setText(f'\'{new_data}\' already exist. Try again.')
            UpdateMessageBox.show()

    def _read_settings(self):

        #self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY, self.saveGeometry()))
        self.gestures = self.settings.value('abbreviations', self.gestures)
        self.reload_gestures(self.gestures)
        self.resize_gesturesTableView_cells()

    def resize_gesturesTableView_cells(self):
        """ Resize the rows and columns of the gesturesTableView. """

        self.gesturesTableView.resizeRowsToContents()
        self.gesturesTableView.resizeColumnsToContents()
        self.gesturesTableView.horizontalHeader().setStretchLastSection(True)

    def reload_gestures(self, gestures: dict):

        active_gestures = len(gestures)
        self.countLabel.setText(f'Active: {active_gestures}')
        print(f'Active: {active_gestures}')
        for gesture, meaning in gestures.items():
            self.determine_gesture(gesture, meaning)
            self.update_gesture_tableview(gesture, meaning)
            print(gesture, meaning)

    def update_gesture_tableview(self, gesture, meaning):
        """ Insert one row at a time in the GestureTableView. """

        TEMP_HEADER['gesture'] = gesture
        TEMP_HEADER['meaning'] = meaning
        RECORD.append(list(TEMP_HEADER.values()))
        self.gesturesTableModel.insertRows(len(RECORD), 1)
        self.resize_gesturesTableView_cells()

    def on_addPushButton_clicked(self):

        try:
            from src.gui.dialogs.add import AddGestureDialog
            dialog = AddGestureDialog(self)
            if dialog.exec():
                # Get user's input
                gesture = dialog.gestureLineEdit.text()
                meaning = dialog.meaningLineEdit.text()

                # Determine what kind of gesture to add
                self.determine_gesture(gesture, meaning)

                # Store newly added gestures in a dictionary
                self.gestures[gesture] = meaning
                self.update_settings()
                self.display_output()   # Display output for debugging

                self.update_gesture_tableview(gesture, meaning)

        except ValueError:
            print(f'\'{gesture}\' already exist. Try again.')
            AddMessageBox.setText(f'\'{gesture}\' already exist. Try again.')
            AddMessageBox.show()

    def determine_gesture(self, gesture, meaning):
        """ Determine what kind of gesture to add base on the given meaning of the user. """

        if 'https://' in meaning or 'http://' in meaning:
            self.has_http(gesture, meaning)
        else:
            # Do the default adding of gesture
            self.keyboardGesture.add_gesture(gesture, meaning)

    def has_http(self, gesture, meaning):
        """ Method that will open a website in a new tab of the default web browser. """

        callback = lambda: wb.open_new_tab(meaning)
        kb.add_word_listener(gesture, callback)

    def on_updatePushButton_clicked(self):
        """ Event handler that update an existing keyboardGesture. """

        try:
            from src.gui.dialogs.update import UpdateGestureDialog
            dialog = UpdateGestureDialog(self)

            if dialog.exec():
                # Get input
                new_gesture = dialog.new_gestureLineEdit.text()
                new_meaning = dialog.new_meaningLineEdit.text()

                # Remove current keyboardGesture
                self.keyboardGesture.remove_gesture(new_gesture)

                self.determine_gesture(new_gesture, new_meaning)
                self.gestures[new_gesture] = new_meaning

                self.update_settings()
                self.display_output()

                # Clear the Gesture TableView first
                self.clear_gestures_tableview()

                # Start re-inserting the updated gestures
                for gesture, meaning in self.gestures.items():
                    self.update_gesture_tableview(gesture, meaning)

        except ValueError:
            print(f'No existing gesture found for \'{new_gesture}\'. Try again.')
            UpdateMessageBox.setText(f'No existing gesture found for \'{new_gesture}\'. Try again.')
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
                del self.gestures[gesture_to_remove]                    # remove internal list of gestures

                self.update_settings()
                self.display_output()

                # Clear the Gesture TableView first
                self.clear_gestures_tableview()

                # Start re-inserting the updated gestures
                for gesture, meaning in self.gestures.items():
                    self.update_gesture_tableview(gesture, meaning)

        except (KeyError, ValueError) as e:
            print(f'No existing gesture found for \'{gesture_to_remove}\'. Try again. -> type: {type(e)}')
            RemoveMessageBox.setText(f'No existing gesture found for \'{gesture_to_remove}\'. Try again.')
            RemoveMessageBox.show()

    def clear_gestures_tableview(self):
        """ Method that will remove the content of the GesturesTableView. """

        # Clear the Gesture TableView first
        self.gesturesTableModel.removeRows(0, len(RECORD))
        self.gesturesTableView.setModel(self.gesturesTableModel)
        RECORD.clear()

    def display_output(self):
        """ Display output in the command line. For debugging purposes. """

        length_active_gestures = len(self.gestures)
        self.countLabel.setText(f'Active: {length_active_gestures}')
        print(f'\nActive: {length_active_gestures}')
        sorted_items = sorted(self.gestures.items())
        for gesture, meaning in sorted_items:
            print(gesture, meaning)

    def closeEvent(self, event):

        self._write_settings()

    def _write_settings(self):

        self.settings.setValue('abbreviations', self.gestures)
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())

    def keyPressEvent(self, event):

        # 'Ctrl+Q: quit the app'
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.close()

    def resizeEvent(self, event):

        #print(f'{self.width()} x {self.height()}')
        pass

    def hook_something(self, something):

        kb.hook(something)
