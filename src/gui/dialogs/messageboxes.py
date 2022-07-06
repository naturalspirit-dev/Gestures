# Message boxes

from PyQt5.QtWidgets import QMessageBox
from src.resources.constant import __appname__

AddMessageBox = QMessageBox()
AddMessageBox.setWindowTitle('Add Gesture Message')
AddMessageBox.setIcon(QMessageBox.Information)

UpdateMessageBox = QMessageBox()
UpdateMessageBox.setWindowTitle('Update Gesture Message')
UpdateMessageBox.setIcon(QMessageBox.Information)

RemoveMessageBox = QMessageBox()
RemoveMessageBox.setWindowTitle('Delete Gesture')
RemoveMessageBox.setIcon(QMessageBox.Warning)
RemoveMessageBox.setText('Do you really want to remove the selected record?')
RemoveMessageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

WarningMessageBox = QMessageBox()
WarningMessageBox.setIcon(QMessageBox.Warning)

AboutMessageBox = QMessageBox()

DDayMessageBox = QMessageBox()
DDayMessageBox.setWindowTitle(f'Unregistered {__appname__}')
DDayMessageBox.setIcon(QMessageBox.Information)
DDayMessageBox.setText('It seems you\'ve reached the limited usage for Gestures. Contact GSMGBB for further info.')
