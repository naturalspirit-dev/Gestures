# Main User Interface of Gestures

import logging
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
                             QSystemTrayIcon,
                             QMessageBox,
                             QComboBox)
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
                                    GesturesData,       # [] TODO: possible refactoring of identifier
                                    SETTINGS_GEOMETRY,
                                    SETTINGS_PROFILE,
                                    SETTINGS_FILENAME,
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
        self.gestures = {}      # This will hold all the existing gestures
        self.old_settings()
        self.new_settings()
        logging.info(self.settings.fileName())       
        self.close_shortcut = False
        self._create_actions()
        self._create_menus()
        self._widgets() 
        self._layout()
        self._read_settings()
        self._properties()
        self._connections()
        self.restoreGeometry(self.settings.value(SETTINGS_GEOMETRY, self.saveGeometry()))

    def old_settings(self):

        from src.resources.constant import APP
        
        APP.setOrganizationName('GIPSC Core Team')
        SETTINGS_PROFILE = 'abbreviations'
        self.settings = QSettings()
        self.old_gestures = self.settings.value(SETTINGS_PROFILE, self.gestures)

    def new_settings(self):

        self.settings = QSettings(SETTINGS_FILENAME, QSettings.IniFormat)

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

        self.profileLabel = QLabel()
        self.profileComboBox = QComboBox()
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

        profile_layout = QHBoxLayout()
        profile_layout.addWidget(self.profileLabel)
        # profile_layout.addWidget(self.profileComboBox)
        profile_layout.addStretch(1)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.addPushButton)
        right_layout.addWidget(self.updatePushButton)
        right_layout.addWidget(self.removePushButton)
        right_layout.addStretch(1)

        left_layout = QVBoxLayout()
        left_layout.addWidget(self.gesturesTableView)
        left_layout.addWidget(self.countLabel)

        table_buttons_layout = QHBoxLayout()
        table_buttons_layout.addLayout(left_layout)
        table_buttons_layout.addLayout(right_layout)

        stack_layout = QVBoxLayout()
        stack_layout.addLayout(profile_layout)
        stack_layout.addLayout(table_buttons_layout)

        self.setLayout(stack_layout)

    def _properties(self):

        self.profileLabel.setText(f'Profile: {SETTINGS_PROFILE}')

        # feed filterModel with main model
        self.gesturesSortFilterProxyModel.setSourceModel(self.gesturesTableModel)

        self.gesturesTableView.setModel(self.gesturesSortFilterProxyModel)
        self.gesturesTableView.setAlternatingRowColors(True)
        self.gesturesTableView.setSortingEnabled(True)
        self.gesturesTableView.sortByColumn(0, Qt.AscendingOrder)
        self.gesturesTableView.setShowGrid(False)
        # self.gesturesTableView.setSelectionModel(self.gesturesItemSelectionModel)     # [] TODO: for deletion? you declared it but you're not using it

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

        # This will trigger by the following scenarios:
        #   1. pressing 'enter'
        #   2. navigation keys (up, down, left, right arrow keys)
        #   3. selecting a different cell via mouse
        self.gesturesTableModel.dataChanged.connect(self.on_gesturesTableModel_dataChanged)

        # When the user clicked or right-clicked the icon in the system tray
        self.gesturesSystemTray.activated.connect(self.on_gesturesSystemTray_activated)

    def update_selectedData(self):

        self.selected_data = self.gesturesTableView.current_data
        logging.info(f'update_selectedData -> {self.gesturesTableView.current_data} x {self.gesturesTableView.previous_data}')

    def update_settings(self):
        """ Update gestures dict for every add, update and delete. """

        # [] TODO: possible benefit: let the user extract his/her gestures for backup purposes
        self.settings.setValue(SETTINGS_PROFILE, self.gestures)

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

        self.gestures = self.settings.value(SETTINGS_PROFILE, self.gestures); logging.info(SETTINGS_PROFILE)
        self.gestures.update(self.old_gestures)
        self.reload_gestures(self.gestures)
        self.resize_gesturesTableView_cells()

    def resize_gesturesTableView_cells(self):
        """ Resize the rows and columns of the gesturesTableView. """

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
        """ Insert rows in gestureTableView. """

        TEMP_HEADER['gesture'] = gesture
        TEMP_HEADER['meaning'] = meaning
        RECORD.append(list(TEMP_HEADER.values()))
        self.gesturesTableModel.insertRows(len(RECORD), 1)
        self.gesturesTableView.setModel(self.gesturesTableModel)

    # [] TODO: gesturesTableView not updating properly when new gesture is updated
    def on_addPushButton_clicked(self):

        try:
            from src.gui.dialogs.add import AddGestureDialog
            dialog = AddGestureDialog(self)
            if dialog.exec():
                # Get user's input
                gesture = dialog.gestureLineEdit.text()
                meaning = dialog.valueLineEdit.text()

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
                new_gesture = dialog.gestureLineEdit.text()
                new_meaning = dialog.valueLineEdit.text()

                # Remove current keyboardGesture
                self.keyboardGesture.remove_gesture(new_gesture)

                self.determine_gesture(new_gesture, new_meaning)
                self.gestures[new_gesture] = new_meaning

                self.update_settings()
                self.display_output()

                # [] TODO: SO: How to get the currentIndex of a QTableView without interacting with it?
                # Clear the Gesture TableView first
                self.clear_gestures_tableview()

                # Start re-inserting the updated gestures
                for gesture, meaning in self.gestures.items():
                    self.update_gesture_tableview(gesture, meaning)

        except (KeyError, ValueError) as e:
            print(f'No existing gesture found for \'{new_gesture}\'. Try again. -> type: {type(e)}')
            UpdateMessageBox.setText(f'No existing gesture found for \'{new_gesture}\'. Try again.')
            UpdateMessageBox.show()

    # [] TODO: crashes when last added row is removed
    def on_removePushButton_clicked(self):
        """ Remove gesture based on selected row(s). """

        try:
            # Get details of selected row to delete
            index = self.gesturesTableView.currentIndex()
            row = index.row()
            col = index.column()
            data = index.data()

            choice = QMessageBox.warning(self, 'Remove Gestures', f'Do you want to remove \'{data}\'?',
                                         QMessageBox.Yes, QMessageBox.No)

            if choice == QMessageBox.Yes:
                # Check if current selection is on the 'Meaning' column
                if col == 1:
                    data = self.get_key(data)

                # Remove keyboardGesture
                self.keyboardGesture.remove_gesture(data)  # raise ValueError when this fails

                del RECORD[row]
                del self.gestures[data]

                self.update_settings()
                self.display_output()

                self.gesturesTableModel.removeRows(row, 1)      # [] TODO/FYI: possible solution to your updatePushButton_clicked fiasco
                self.gesturesTableView.setModel(self.gesturesTableModel)

        except (KeyError, ValueError, Exception) as e:
            print(f'No existing gesture found for \'{data}\'. Try again. -> type: {type(e)}')
            RemoveMessageBox.setText(f'No existing gesture found for \'{data}\'. Try again.')
            RemoveMessageBox.show()

    def get_key(self, meaning):
        """ Return corresponding key of selected 'meaning' """

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

    def on_gesturesSystemTray_activated(self, activation_reason):

        if activation_reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.show()

    def closeEvent(self, event):

        if self.close_shortcut or isinstance(self.sender(), QAction):
            self._write_settings()
            self.gesturesSystemTray.hide()
            event.accept()
        else:
            self.hide()
            # [] TODO: check if the app is running on Win10 to determine what appropriate message to show in the system tray
            #          Win 10 - shows a sliding pop-up
            #          Win 7 - still shows in a baloon like Win XP
            self.gesturesSystemTray.showMessage('Gestures', 'I\'m still running. You can access me in the system tray',
                                                QSystemTrayIcon.Information,
                                                3000)
            print('Gestures is now running in the background')
            event.ignore()

    def _write_settings(self):

        self.settings.setValue(SETTINGS_PROFILE, self.gestures)
        self.settings.setValue(SETTINGS_GEOMETRY, self.saveGeometry())

    def keyPressEvent(self, event):

        # 'Ctrl+Q: quit the app'
        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.close_shortcut = True
            self.close()

    def hook_something(self, something):

        kb.hook(something)
