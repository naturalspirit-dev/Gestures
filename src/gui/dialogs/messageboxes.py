# Message boxes

from string import Template
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMessageBox
from src.resources import gestures_resources
from src.resources.constant import (__appname__,
                                    __version__,
                                    python_version,
                                    PYQT_VERSION_STR,
                                    QT_VERSION_STR,
                                    KEYBOARD_VERSION)


AddMessageBox = QMessageBox()
AddMessageBox.setWindowTitle('Add Gesture Message')
AddMessageBox.setIcon(QMessageBox.Information)

UpdateMessageBox = QMessageBox()
UpdateMessageBox.setWindowTitle('Update Gesture Message')
UpdateMessageBox.setIcon(QMessageBox.Information)

RemoveMessageBox = QMessageBox()
RemoveMessageBox.setWindowTitle('Delete Gesture')
RemoveMessageBox.setWindowIcon(QIcon(':g-key-32.png'))
RemoveMessageBox.setIcon(QMessageBox.Warning)
RemoveMessageBox.setText('Do you really want to remove the selected record?')
RemoveMessageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

WarningMessageBox = QMessageBox()
WarningMessageBox.setIcon(QMessageBox.Warning)

AboutMessageBox = QMessageBox()
AboutMessageBox.setWindowIcon(QIcon(':/g-key-32.png'))
AboutMessageBox.setIconPixmap(QPixmap(':/g-key-32.png'))
AboutMessageBox.setWindowTitle(f'About {__appname__}')
AboutMessageBox.setText(f'<b>{__appname__} {__version__}</b>')
about_template = Template("""
<p>An application for people who just loved to type.</p>
<hr>
<p>
    <b>Dependencies</b><br><br>
    Python $PYTHON_VERSION<br>
    PyQt $PYQT_VERSION<br>
    Qt $QT_VERSION<br>
    keyboard $KEYBOARD_VERSION
</p>
<p>
    <b>Contacts</b><br><br>
    Jero Bado<br>
    say.hello@jerobado.com<br>
    <a href="https://jerobado.com">https://jerobado.com</a>
<p>
""")
about_versions = {
    'PYTHON_VERSION': python_version(),
    'PYQT_VERSION': PYQT_VERSION_STR,
    'QT_VERSION': QT_VERSION_STR,
    'KEYBOARD_VERSION': KEYBOARD_VERSION
}
about_details = about_template.substitute(about_versions)
AboutMessageBox.setInformativeText(about_details)

DDayMessageBox = QMessageBox()
DDayMessageBox.setWindowTitle(f'Unregistered {__appname__}')
DDayMessageBox.setIcon(QMessageBox.Information)
DDayMessageBox.setText('It seems you\'ve reached the limited usage for Gestures. Contact GSMGBB for further info.')
