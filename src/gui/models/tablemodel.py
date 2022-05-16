from PyQt5.QtCore import (Qt,
                          QAbstractTableModel,
                          QModelIndex)


class GesturesTableModel(QAbstractTableModel):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.headers = ['Gesture', 'Value']
        self.records = []

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def data(self, index, role):

        row, col = index.row(), index.column()

        if role == Qt.DisplayRole:
            return self.records[row][col]

    def columnCount(self, parent):

        return len(self.headers)

    def rowCount(self, parent):

        return len(self.records)

    def insertRows(self, position, rows, parent=QModelIndex()):

        self.beginInsertRows(parent, position, position + rows - 1)
        self.endInsertRows()
        return True
