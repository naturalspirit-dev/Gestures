from PyQt5.QtCore import (Qt,
                          QAbstractTableModel,
                          QModelIndex)
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.domain.repositories import keyboardGestureRepository


class GesturesTableModel(QAbstractTableModel):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.headers = ['ID', 'Shorthand', 'Value', 'Date Created', 'Last Update']
        self.initializeTableModel()

    def initializeTableModel(self):

        records = keyboardGestureRepository.getAllGestures()
        self.insertRows(len(records), 1)

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]

    def data(self, index, role):

        row, col = index.row(), index.column()

        if role == Qt.DisplayRole:
            try:
                record = keyboardGestureRepository.keyboardGestureList[row]
                cell = record.values[col]
                return cell
            except IndexError:
                return None

    def columnCount(self, parent):

        return len(self.headers)

    def rowCount(self, parent):

        return keyboardGestureRepository.count()

    def insertRows(self, position, rows, parent=QModelIndex()):

        self.beginInsertRows(parent, position, position + rows - 1)
        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QModelIndex()):

        self.beginRemoveRows(parent, position, rows)
        self.endRemoveRows()
        return True

    def addRecord(self, gesture: KeyboardGesture):

        keyboardGestureRepository.addRecord(gesture)
        self.insertRows(keyboardGestureRepository.count(), 1)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        keyboardGestureRepository.updateRecord(index, gesture)

    def removeRecord(self, index: int):

        keyboardGestureRepository.removeRecord(index)
        self.removeRows(index, index)
