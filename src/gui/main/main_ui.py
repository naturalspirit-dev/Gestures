# Main User Interface of Gestures

import keyboard as kb
import webbrowser as wb
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QLabel,
                             QAction,
                             QMenu,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QWidget,
                             QTableView,        # [] TODO: unused widget due to re-implemanation of GesturesTableView
                             QSystemTrayIcon)
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
                                    __version__,
                                    GesturesData,
                                    SETTINGS_GEOMETRY,
                                    TEMP_HEADER)
from src.resources import gestures_resources
from src.resources.models import GestureTableModel

RECORD = GesturesData.RECORD


class GesturesWindow(QWidget):
    """ Gestures' main user interface. """

    def __init__(self, parent=None):

        super().__init__(parent)
        self.keyboardGesture = KeyboardGesture()
        self.selected_data = None
        self.settings = QSettings()
        self.gestures = {}      # This will hold all the existing gestures
        self.close_shortcut = False
        self._create_actions()
        self._create_menus()
        self._widgets()
        self._layout()
        self._read_settings()
        self._properties()
        self._connections()
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY, self.saveGeometry()))

    def _create_actions(self):

        self.openGesturesAction = QAction('Open Gestures', self,
                                          triggered=self.on_openGestures_action)
        self.quitGesturesAction = QAction('Quit Gestures', self,
                                          shortcut='ctrl+q',
                                          triggered=self.close)

    def on_openGestures_action(self):

        if self.isHidden():
            self.show()

    def _create_menus(self):

        # System Tray menu
        self.gesturesMenu = QMenu()
        self.gesturesMenu.addAction(self.openGesturesAction)
        self.gesturesMenu.addSeparator()
        self.gesturesMenu.addAction(self.quitGesturesAction)

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
        self.gesturesSystemTray = QSystemTrayIcon()

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

        # feed filterModel with main model
        self.gesturesSortFilterProxyModel.setSourceModel(self.gesturesTableModel)

        self.gesturesTableView.setModel(self.gesturesSortFilterProxyModel)
        self.gesturesTableView.setAlternatingRowColors(True)
        self.gesturesTableView.setSortingEnabled(True)
        self.gesturesTableView.sortByColumn(0, Qt.AscendingOrder)
        self.gesturesTableView.setShowGrid(False)
        # self.gesturesTableView.setSelectionModel(self.gesturesItemSelectionModel)

        # TEST: adding a system tray icon
        self.gesturesSystemTray.setIcon(QIcon(':/g-key-32.png'))
        self.gesturesSystemTray.setToolTip(f'{__appname__} {__version__}')
        self.gesturesSystemTray.setContextMenu(self.gesturesMenu)
        self.gesturesSystemTray.show()

        self.addPushButton.setText('&Add')
        self.updatePushButton.setText('&Update')
        # self.removePushButton.setEnabled(False)
        self.removePushButton.setText('&Remove')
        self.resize(409, 364)   # width, height
        self.setWindowTitle(f'{__appname__} {__version__}')
        self.setWindowIcon(QIcon(':/g-key-32.png'))

    def _connections(self):

        self.addPushButton.clicked.connect(self.on_addPushButton_clicked)
        self.updatePushButton.clicked.connect(self.on_updatePushButton_clicked)
        self.removePushButton.clicked.connect(self.on_removePushButton_clicked)

        # When the user interacts with the table using the tab or arrow keys
        self.gesturesTableView.activated.connect(self.update_selectedData)
        self.gesturesTableView.clicked.connect(self.update_selectedData)
        self.gesturesTableView.doubleClicked.connect(self.update_selectedData)

        # This will trigger after (1) pressing 'enter', (2) navigation keys (3) or selecting a different cell
        self.gesturesTableModel.dataChanged.connect(self.on_gesturesTableModel_dataChanged)

        # TEST: for tennySystemTray signals and slots
        self.gesturesSystemTray.activated.connect(self.on_gesturesSystemTray_activated)

    def update_selectedData(self):

        self.selected_data = self.gesturesTableView.current_data
        print(f'update_selectedData -> {self.gesturesTableView.current_data} x {self.gesturesTableView.previous_data}')

    def update_settings(self):
        """ Update gestures dict for every add, update and delete. """

        self.settings.setValue('abbreviations', self.gestures)

    def on_gesturesTableModel_dataChanged(self):

        # [] TODO: Beautify this code when you come back from vacation.
        index = self.gesturesTableView.currentIndex()
        row = index.row()
        col = index.column()
        new_data = index.data()
        self.selected_data = self.gesturesTableView.current_data
        print(f'on_dataChanged: new data -> {new_data}\n\tselected data -> {self.selected_data}')

        try:
            # Check first if the new_data is an existing gesture
            if new_data in self.gestures.keys():
                RECORD[row][col] = self.selected_data
                raise ValueError

            # Get key of edited data -> this will update only the 'meaning'
            for gesture, meaning in self.gestures.items():
                # [] TODO/FYI: you are searching a gesture per row instead of per column
                if self.selected_data in (gesture, meaning):
                    print(f'"{self.selected_data}" found in ({gesture}, {meaning})')
                    # Remove current keyboardGesture
                    self.keyboardGesture.remove_gesture(gesture)
                    print(f'deleting {self.gestures[gesture]}')
                    del self.gestures[gesture]

                    # Add new keyboardGesture
                    # check if data to be edited is the key
                    # [] TODO/FYI: try using a dictionary, just get the column index to identify the key or meaning
                    if self.selected_data == gesture:
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
                    print(f'{self.selected_data} not found in self.gestures')

        except ValueError:
            print(f'\'{new_data}\' already exist. Try again.')
            UpdateMessageBox.setText(f'\'{new_data}\' already exist. Try again.')
            UpdateMessageBox.show()

    def _read_settings(self):

        self.gestures = self.settings.value('abbreviations', self.gestures)
        self.reload_gestures(self.gestures)
        self.resize_gesturesTableView_cells()

    def resize_gesturesTableView_cells(self):
        """ Resize the rows and columns of the gesturesTableView. """

        # self.gesturesTableView.resizeRowsToContents()
        # self.gesturesTableView.resizeColumnsToContents()
        self.gesturesTableView.horizontalHeader().setStretchLastSection(True)

    def reload_gestures(self, gestures: dict):

        active_gestures = len(gestures)
        self.countLabel.setText(f'Active: {active_gestures}')
        print(f'Active: {active_gestures}')
        for gesture, meaning in gestures.items():
            self.determine_gesture(gesture, meaning)
            self.update_gesture_tableview(gesture, meaning)
            print(gesture, meaning)

    # [] TODO: insert a for loop here, too much for loop outside
    # [] TODO: sort not working after adding, updating and removing a gesture
    def update_gesture_tableview(self, gesture, meaning):
        """ Insert one row at a time in the GestureTableView. """

        TEMP_HEADER['gesture'] = gesture
        TEMP_HEADER['meaning'] = meaning
        RECORD.append(list(TEMP_HEADER.values()))
        self.gesturesTableModel.insertRows(len(RECORD), 1)
        self.gesturesTableView.setModel(self.gesturesTableModel)

    # [] TODO: gesturesTableView not updating properly when new gesture is update
    def on_addPushButton_clicked(self):

        try:
            from src.gui.dialogs.add import AddGestureDialog
            dialog = AddGestureDialog(self)
            if dialog.exec():
                # Get user's input
                gesture = dialog.gestureLineEdit.text()
                meaning = dialog.meaningLineEdit.text()

                # TEST: check if the user is adding an existing gesture
                if gesture in self.gestures.keys():
                    raise ValueError

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

        except (KeyError, ValueError) as e:
            print(f'No existing gesture found for \'{new_gesture}\'. Try again. -> type: {type(e)}')
            UpdateMessageBox.setText(f'No existing gesture found for \'{new_gesture}\'. Try again.')
            UpdateMessageBox.show()

    def on_removePushButton_clicked(self):
        """ Remove gesture based on selected row(s). """

        try:
            # Get details of selected row to delete
            index = self.gesturesTableView.currentIndex()
            row = index.row()
            col = index.column()
            data = index.data()

            # Check if current selection is on the 'Meaning' column
            if col == 1:
                data = self.get_key(data)

            # Remove keyboardGesture
            self.keyboardGesture.remove_gesture(data)  # raise ValueError when this fails
            print(f'deleted {data}')
            del self.gestures[data]  # remove internal list of gestures

            self.update_settings()
            self.display_output()

            # Clear the Gesture TableView first
            self.clear_gestures_tableview()

            # Start re-inserting the updated gestures
            for gesture, meaning in self.gestures.items():
                self.update_gesture_tableview(gesture, meaning)

        except (KeyError, ValueError, Exception) as e:
            print(f'No existing gesture found for \'{data}\'. Try again. -> type: {type(e)}')
            RemoveMessageBox.setText(f'No existing gesture found for \'{data}\'. Try again.')
            RemoveMessageBox.show()

    def get_key(self, meaning):

        for k, v in self.gestures.items():
            if meaning in (k, v):
                return k

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

    def on_gesturesSystemTray_activated(self):

        # [] TODO: identify if the user use left or right-click
        if self.isHidden():
            self.show()

    def mousePressEvent(self, event):

        if Qt.LeftButton:
            print('left-clicked')
        elif Qt.RightButton:
            print('right-clicked')

    def closeEvent(self, event):

        if self.close_shortcut or isinstance(self.sender(), QAction):
            self._write_settings()
            self.gesturesSystemTray.hide()
            event.accept()
        else:
            self.hide()
            self.gesturesSystemTray.showMessage('Gestures', 'I\'m still running. You can access me in the system tray',
                                                QSystemTrayIcon.Information,
                                                3000)
            print('Gestures now running in the background')
            event.ignore()

    def _write_settings(self):

        self.settings.setValue('abbreviations', self.gestures)
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())

    def keyPressEvent(self, event):

        # 'Ctrl+Q: quit the app'
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.close_shortcut = True
            self.close()

    # [] TODO: no practical use, just delete this
    def resizeEvent(self, event):

        #print(f'{self.width()} x {self.height()}')
        pass

    def hook_something(self, something):

        kb.hook(something)
