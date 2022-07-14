from PyQt5.QtCore import QModelIndex, QSettings, QSize, QPoint
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import QAction, QMainWindow

from src.domain.services import keyboardGestureService
from src.gui.dialogs.messageboxes import RemoveMessageBox, AboutMessageBox
from src.gui.widgets.menubar import GesturesMenuBar
from src.gui.widgets.statusbar import GesturesStatusBar
from src.gui.widgets.tableview import NewGesturesTableView
from src.resources import gestures_resources
from src.resources.constant import __appname__


class GesturesMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._set_widgets()
        self._set_properties()
        self._set_connections()
        self._read_settings()

    def _read_settings(self):

        self.settings = QSettings()
        self.settings.beginGroup('GesturesMainWindow')
        self.resize(self.settings.value('size', QSize(700, 400)))
        self.move(self.settings.value('pos', QPoint(200, 200)))
        self.settings.endGroup()

    def _write_settings(self):

        self.settings.beginGroup('GesturesMainWindow')
        self.settings.setValue('size', self.size())
        self.settings.setValue('pos', self.pos())
        self.settings.endGroup()

    def _set_widgets(self):

        self.gesturesMenuBar = GesturesMenuBar(self)
        self.gesturesTableView = NewGesturesTableView(self)
        self.gesturesStatusBar = GesturesStatusBar(self)
        self.setMenuBar(self.gesturesMenuBar)
        self.setCentralWidget(self.gesturesTableView)
        self.setStatusBar(self.gesturesStatusBar)

    def _set_properties(self):

        self.setWindowIcon(QIcon(':/g-key-32.png'))
        self.setWindowTitle(__appname__)
        self.resize(700, 400)

    def _set_connections(self):

        self.gesturesMenuBar.fileMenu.newAction.triggered.connect(self.on_newAction_triggered)
        self.gesturesMenuBar.fileMenu.quitAction.triggered.connect(self.close)
        self.gesturesMenuBar.editMenu.updateAction.triggered.connect(self.on_updateAction_triggered)
        self.gesturesMenuBar.editMenu.deleteAction.triggered.connect(self.on_deleteAction_triggered)
        self.gesturesMenuBar.helpMenu.aboutAction.triggered.connect(self.on_aboutAction_triggered)

    # Slots
    def on_newAction_triggered(self):

        new_gesture = self.gesturesMenuBar.fileMenu.newAction.showAddGestureDialog()
        if new_gesture:
            validation = keyboardGestureService.validateGesture(new_gesture)
            if validation.is_valid:
                self.gesturesTableView.addRecord(new_gesture)
                self.updateStatusBar('new')
            else:
                validation.showValidationDialog()

    def on_updateAction_triggered(self):

        selected_index = self.gesturesTableView.currentIndex()
        validation = keyboardGestureService.validateSelectedIndex(selected_index, 'update')
        if validation.is_valid:
            self.updateRecord(selected_index)
        else:
            validation.showValidationDialog()

    def updateRecord(self, index: QModelIndex):

        updated_gesture = self.gesturesMenuBar.editMenu.updateAction.showUpdateGestureDialog(index)
        if updated_gesture:
            validation = keyboardGestureService.validateGestureOnUpdate(index, updated_gesture)
            if validation.is_valid:
                self.gesturesTableView.updateRecord(index.row(), updated_gesture)
                self.updateStatusBar('update')
            else:
                validation.showValidationDialog()

    def on_deleteAction_triggered(self):

        selected_index = self.gesturesTableView.currentIndex()
        validation = keyboardGestureService.validateSelectedIndex(selected_index, 'delete')
        if validation.is_valid:
            self.deleteRecord(selected_index)
        else:
            validation.showValidationDialog()

    def deleteRecord(self, index: QModelIndex):

        choice = RemoveMessageBox.exec()
        if choice == RemoveMessageBox.Yes:
            self.gesturesTableView.removeRecord(index.row())
            self.updateStatusBar('delete')

    def on_quitAction_triggered(self):

        self.close()

    def on_aboutAction_triggered(self):

        AboutMessageBox.show()

    def updateStatusBar(self, action: str):

        if action == 'new':
            self.setActiveGesturesCountLabel()
            self.gesturesStatusBar.displayMessage('New gesture added.')
        elif action == 'update':
            self.gesturesStatusBar.displayMessage('Selected gesture updated.')
        elif action == 'delete':
            self.setActiveGesturesCountLabel()
            self.gesturesStatusBar.displayMessage('Selected gesture deleted.')

    def setActiveGesturesCountLabel(self):

        records = keyboardGestureService.getTotalRecords()
        self.gesturesStatusBar.activeGesturesCountLabel.setText(f'Active: {records}')

    def closeEvent(self, event: QCloseEvent):

        if isinstance(self.sender(), QAction):
            # executed when:
            # - using File > Quit menu
            # - using Ctrl+Q shortcut keys
            self._write_settings()
            event.accept()
        else:
            # executed when (while window is opened, minimized or closed):
            # - using Quit menu in the system tray
            # - using Alt+F4 shortcut keys
            self.hide()
            event.ignore()
