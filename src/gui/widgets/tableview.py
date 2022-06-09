# Re-implementing QTableView

from PyQt5.QtWidgets import QTableView
from src.domain.entities.keyboard_gesture import KeyboardGesture
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
        self.setModel(self.gesturesTableModel)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.resizeColumnToContents(0)
        self.resizeRowsToContents()

    def addRecord(self, gesture: KeyboardGesture):

        self.gesturesTableModel.addRecord(gesture)
        self.setModel(self.gesturesTableModel)
        self.resizeRowsToContents()

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        self.gesturesTableModel.updateRecord(index, gesture)
        self.setModel(self.gesturesTableModel)

    def removeRecord(self, index: int):

        self.gesturesTableModel.removeRecord(index)
        self.setModel(self.gesturesTableModel)

    def currentChanged(self, current_index, previous_index):

        # TODO: get the current index's row and data based on Update or Delete menu
        previous = previous_index.data()
        current = current_index.data()

        print(f'{previous=}')
        print(f'row: {current_index.row()}: {current=}')
        print()
