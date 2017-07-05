import sys
import unittest

import keyboard as kb
from PyQt5.QtWidgets import QApplication

sys.path.append('..')
APP = QApplication(sys.argv)


class GesturesTest(unittest.TestCase):
    """ Testing the core of the application. """

    def setUp(self):
        from src.core.gestures import Gestures
        self.app = Gestures()

    def test_add_gestures_return_result(self):
        """ Test if self.add_gestures will return a dictionary. """

        result = self.app.get_gestures('xx', 'xxxxx')
        self.assertIsInstance(result, dict)

    def test_check_argument_type_result(self):
        """ Should return True if self.abbv and self.equivalent are both str type. """

        result = self.app.check_argument_type('x', 'jerobado')
        self.assertTrue(result)

    def test_check_argument_type_for_abbv(self):
        """ Should return False if self.abbv is not str """

        result = self.app.check_argument_type(1, 'jerobado')
        self.assertFalse(result)

    def test_check_argument_type_for_equivalent(self):
        """ Should return False if self.equivalent is not str """

        result = self.app.check_argument_type('jerobado', 1)
        self.assertFalse(result)

    def test_add_gesture_to_keyboard(self):
        """ Test if newly added gesture has been added in the keyboard library. """

        self.app.get_gestures('x', 'jerobado')
        self.app.add_gesture_to_keyboard()
        result = self.app.abbv in kb._word_listeners
        self.assertTrue(result)

    def test_check_unique_gesture_if_true(self):
        """ Test if newly added abbreviation DOES NOT exist in the keyboard library."""

        result = self.app.check_unique_gesture('z')
        self.assertTrue(result)

    def test_check_unique_gesture_if_false(self):
        """ Test if newly added abbreviation DO exist in the keyboard libarary. """

        result = self.app.check_unique_gesture('x')
        self.assertFalse(result)

    def test_show_gesture(self):
        """ Test if gestures has been printed. """

        result = self.app.show_gestures()
        self.assertIsNone(result)

    def test_current_version(self):
        """ Test for current version. """

        current_version = '1.1'
        result = self.app.__version__
        self.assertEqual(result, current_version)


class GesturesUITest(unittest.TestCase):
    """ Testing the UI of Gestures. """

    def setUp(self):
        from src.gui.main_window import GesturesUI
        self.window = GesturesUI()

    def test_check_fields_empty(self):
        """ Test if add pushbutton is disabled, should return False. """

        self.window.abbvLineEdit.setText('')
        self.window.equivLineEdit.setText('')
        self.window.check_fields()
        result = self.window.addPushButton.isEnabled()
        self.assertFalse(result)
        print('test_check_fields_empty: {}'.format(result))

    def test_check_fields_not_empty(self):
        """ Test add pushbutton is enabled if both fiels are not empty, should return True. """

        self.window.abbvLineEdit.setText('1')
        self.window.equivLineEdit.setText('2')
        self.window.check_fields()
        result = self.window.addPushButton.isEnabled()
        self.assertTrue(result)
        print('test_check_fields_not_empty: {}'.format(result))

    def test_check_fields_abbvLineEdit_empty(self):
        """ Test add pushbutton is disabled if abbvLineEdit is empty, should return False. """

        self.window.abbvLineEdit.setText('')
        self.window.equivLineEdit.setText('2')
        self.window.check_fields()
        result = self.window.addPushButton.isEnabled()
        self.assertFalse(result)
        print('test_check_fields_abbvLineEdit_empty: {}'.format(result))

    def test_check_fields_equivLineEdit_empty(self):
        """ Test add pushbutton is disabled if equivLineEdit is empty, should return False. """

        self.window.abbvLineEdit.setText('1')
        self.window.equivLineEdit.setText('')
        self.window.check_fields()
        result = self.window.addPushButton.isEnabled()
        self.assertFalse(result)
        print('test_check_fields_equivLineEdit_empty: {}'.format(result))


if __name__ == '__main__':
    unittest.main()