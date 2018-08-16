# Re-implementing QTableView

from PyQt5.QtWidgets import QTableView


class GesturesTableView(QTableView):

    # selected_data = None

    # def selectionChanged(self, selected, deselected):
    #
    #     index = self.currentIndex()
    #     print(f'selected data -> {self.selected_data}')
    #     # selected_data = selected.data()
    #     # deselected_data = deselected.data()
    #     # print(f'selectionChanged -> {selected_data} x {deselected_data}')

    def currentChanged(self, current, previous):

        self.current_data = current.data()
        self.previous_data = previous.data()
        print(f'currentChanged -> {self.current_data} x {self.previous_data}')
