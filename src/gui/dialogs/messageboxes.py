# Message boxes

from PyQt5.QtWidgets import QMessageBox

AddMessageBox = QMessageBox()
AddMessageBox.setWindowTitle('Add Gesture Message')
AddMessageBox.setIcon(QMessageBox.Information)

UpdateMessageBox = QMessageBox()
UpdateMessageBox.setWindowTitle('Update Gesture Message')
UpdateMessageBox.setIcon(QMessageBox.Information)

RemoveMessageBox = QMessageBox()
RemoveMessageBox.setWindowTitle('Remove Gesture Message')
RemoveMessageBox.setIcon(QMessageBox.Information)
