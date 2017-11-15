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

        if role == Qt.EditRole:
            return RECORD[row][col]

    def setData(self, index, value, role=Qt.DisplayRole):

        if role == Qt.EditRole:
            row = index.row()
            col = index.column()
            RECORD[row][col] = value
            #print(f'on data() -> {RECORD}')
            self.dataChanged.emit(index, index, [])
            return True

    def flags(self, index):

        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def columnCount(self, parent):

        return len(self.header)

    def rowCount(self, parent):

        return len(RECORD)

    def insertRows(self, position, rows, parent=QModelIndex()):

        self.beginInsertRows(parent, position, position + rows - 1)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QModelIndex()):

        self.beginRemoveRows(parent, position, position + rows - 1)
        self.endRemoveRows()
        return True
