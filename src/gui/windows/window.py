from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow
from src.gui.widgets.menubar import GesturesMenuBar
from src.gui.widgets.tableview import NewGesturesTableView


class GesturesMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.values = list
        self._set_widgets()
        self._set_properties()
        self._set_connections()

    def _set_widgets(self):

        self.gesturesMenuBar = GesturesMenuBar(self)
        self.gesturesTableView = NewGesturesTableView(self)

        self.setMenuBar(self.gesturesMenuBar)
        self.setCentralWidget(self.gesturesTableView)

    def _set_properties(self):

        self.setWindowTitle('Gestures')
        self.resize(700, 400)

    def _set_connections(self):

        self.gesturesMenuBar.fileMenu.newAction.triggered.connect(self.on_newAction_triggered)

    def on_newAction_triggered(self):

        # [] TODO: learn how to insert record in the table view model
        # get values from add gestures dialog
        shorthand = self.gesturesMenuBar.fileMenu.newAction.addGesturesDialog.gestureLineEdit.text()
        value = self.gesturesMenuBar.fileMenu.newAction.addGesturesDialog.valueLineEdit.text()

        self.gesturesTableView.gesturesTableModel.insertRows(1, 1)
        self.gesturesTableView.setModel(self.gesturesTableView.gesturesTableModel)
