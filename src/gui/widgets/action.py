from PyQt5.QtWidgets import QAction


class QuitAction(QAction):

    def __init__(self, parent):

        super().__init__('&Quit', parent)
        self.setShortcut('ctrl+q')
