# Gesture Models

from PyQt5.QtCore import (Qt,
                          QModelIndex,
                          QAbstractTableModel)
from src.resources.constant import RECORD


class GestureTableModel(QAbstractTableModel):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.header = ['Gesture', 'Equivalent']

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.header[section]

    def data(self, index, role):

        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            value = RECORD[row][col]
            return value

    def columnCount(self, parent):

        return len(self.header)

    def rowCount(self, parent):

        return len(RECORD)

    def insertRows(self, position, rows, parent=QModelIndex()):

        self.beginInsertRows(parent, position, position + rows - 1)
        self.endInsertRows()
        return True
