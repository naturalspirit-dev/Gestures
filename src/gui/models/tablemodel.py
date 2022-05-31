from PyQt5.QtCore import (Qt,
                          QAbstractTableModel,
                          QModelIndex)
from src.domain.repositories import keyboardGestureRepository


class GesturesTableModel(QAbstractTableModel):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.headers = ['Gesture', 'Value']

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def data(self, index, role):

        row, col = index.row(), index.column()

        if role == Qt.DisplayRole:
            try:
                return keyboardGestureRepository.keyboardGestureList[row][col]
            except IndexError:
                return None

    def columnCount(self, parent):

        return len(self.headers)

    def rowCount(self, parent):

        return len(keyboardGestureRepository.keyboardGestureList)

    def insertRows(self, position, rows, parent=QModelIndex()):

        self.beginInsertRows(parent, position, position + rows - 1)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QModelIndex()):

        self.beginRemoveRows(parent, position, rows)
        self.endRemoveRows()
        return True
