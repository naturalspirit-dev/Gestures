# Re-implementing QTableView

from PyQt5.QtWidgets import QTableView


class GesturesTableView(QTableView):

    current_data = None
    previous_data = None

    def currentChanged(self, current, previous):
        """ Reimplemented slot that will get the current_data and previous_data. """

        self.current_data = current.data()
        self.previous_data = previous.data()
        print(f'currentChanged -> {self.current_data} x {self.previous_data}')
