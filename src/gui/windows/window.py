from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow


class GesturesMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._set_widgets()
        self._set_layouts()
        self._set_properties()
        self._set_connections()

    def _set_widgets(self): pass

    def _set_layouts(self): pass

    def _set_properties(self):

        self.setWindowTitle('Gestures')
        self.resize(700, 400)

    def _set_connections(self): pass

    def keyPressEvent(self, event):

        if event.modifiers() & Qt.ControlModifier and event.key() == Qt.Key_Q:
            self.close()
