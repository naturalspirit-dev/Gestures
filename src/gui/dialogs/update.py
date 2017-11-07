# Update Gesture Dialog

from PyQt5.QtWidgets import (QDialog,
                             QLabel,
                             QLineEdit,
                             QPushButton,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout)


class UpdateGestureDialog(QDialog):

    def __init__(self, parent=None):

        super().__init__(parent)
        self._widgets()
        self._properties()
        self._layout()
        self._connections()

    def _widgets(self):

        self.currentLabel = QLabel()
        self.current_abbvLineEdit = QLineEdit()
        self.current_equivLineEdit = QLineEdit()
        self.newLabel = QLabel()
        self.new_abbvLineEdit = QLineEdit()
        self.new_equivLineEdit = QLineEdit()
        self.okPushButton = QPushButton()

    def _properties(self):

        self.currentLabel.setText('Current Gesture:')
        self.current_abbvLineEdit.setPlaceholderText('abbreviation')
        self.current_equivLineEdit.setPlaceholderText('equivalent')
        self.newLabel.setText('New Gesture:')
        self.new_abbvLineEdit.setPlaceholderText('abbreviation')
        self.new_equivLineEdit.setPlaceholderText('equivalent')
        self.okPushButton.setText('&OK')
        self.setWindowTitle('Update Gesture')

    def _layout(self):

        grid = QGridLayout()   # 2 x 3
        grid.addWidget(self.currentLabel, 0, 0)
        grid.addWidget(self.current_abbvLineEdit, 0, 1)
        grid.addWidget(self.current_equivLineEdit, 0, 2)
        grid.addWidget(self.newLabel, 1, 0)
        grid.addWidget(self.new_abbvLineEdit, 1, 1)
        grid.addWidget(self.new_equivLineEdit, 1, 2)

        third_layer = QHBoxLayout()
        third_layer.addStretch()
        third_layer.addWidget(self.okPushButton)

        stack_layers = QVBoxLayout()
        stack_layers.addLayout(grid)
        stack_layers.addLayout(third_layer)

        self.setLayout(stack_layers)

    def _connections(self):

        self.okPushButton.clicked.connect(self.accept)
