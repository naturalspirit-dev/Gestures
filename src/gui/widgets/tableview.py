# Re-implementing QTableView
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QTableView
from src.domain.entities.keyboard import KeyboardGesture
from src.gui.models.tablemodel import GesturesTableModel


class GesturesTableView(QTableView):

    current_data = None
    previous_data = None

    def currentChanged(self, current, previous):
        """ Reimplemented slot that will get the current_data and previous_data. """

        self.current_data = current.data()
        self.previous_data = previous.data()
        self.scrollTo(self.currentIndex())
        print(f'currentChanged -> {self.current_data} x {self.previous_data}')


class NewGesturesTableView(QTableView):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.gesturesTableModel = GesturesTableModel(self)
        self.sortingProxyModel = QSortFilterProxyModel()
        self._set_model()
        self._set_properties()

    def _set_model(self):

        self.sortingProxyModel.setSourceModel(self.gesturesTableModel)
        self.setModel(self.sortingProxyModel)

    def _set_properties(self):

        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def addRecord(self, gesture: KeyboardGesture):

        self.gesturesTableModel.addRecord(self.sortingProxyModel.rowCount(), gesture)
        self._set_model()
        self.resizeColumnToContents(2)              # Value column
        self.resizeColumnToContents(3)              # Date Created column
        self.resizeRowsToContents()

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        row = self.sortingProxyModel.mapToSource(self.currentIndex()).row()
        self.gesturesTableModel.updateRecord(row, gesture)
        self._set_model()

    def removeRecord(self, index: int):

        row = self.sortingProxyModel.mapToSource(self.currentIndex()).row()
        self.gesturesTableModel.removeRecord(row)
        self._set_model()

    def recordCount(self, index):

        return self.gesturesTableModel.rowCount(index)
