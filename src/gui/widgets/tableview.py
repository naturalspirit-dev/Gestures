# Re-implementing QTableView
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QModelIndex
from PyQt5.QtWidgets import QTableView
from src.domain.entities.keyboard import KeyboardGesture
from src.gui.models.tablemodel import GesturesTableModel


class GesturesTableView(QTableView):

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

    def updateRecord(self, index: QModelIndex, gesture: KeyboardGesture):

        row = self.sortingProxyModel.mapToSource(index).row()
        self.gesturesTableModel.updateRecord(row, gesture)
        self._set_model()

    def removeRecord(self, index: QModelIndex):

        row = self.sortingProxyModel.mapToSource(index).row()
        self.gesturesTableModel.removeRecord(row)
        self._set_model()

    def recordCount(self, index):

        return self.gesturesTableModel.rowCount(index)
