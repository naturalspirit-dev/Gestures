import unittest
from datetime import datetime
from src.domain.entities.keyboard import KeyboardGesture


class TestKeyboardGesture(unittest.TestCase):

    def test_empty_if_true(self):

        empty_gesture = KeyboardGesture(shorthand='',
                                        value='',
                                        date_created=datetime.today().strftime('%x %X %p'),
                                        date_updated=datetime.today().strftime('%x %X %p'))

        empty_shorthand = KeyboardGesture(shorthand='',
                                          value='x',
                                          date_created=datetime.today().strftime('%x %X %p'),
                                          date_updated=datetime.today().strftime('%x %X %p'))

        empty_value = KeyboardGesture(shorthand='x',
                                      value='',
                                      date_created=datetime.today().strftime('%x %X %p'),
                                      date_updated=datetime.today().strftime('%x %X %p'))

        empty_gesture_result = empty_gesture.empty()
        empty_shorthand_result = empty_shorthand.empty()
        empty_value_result = empty_value.empty()

        self.assertTrue(empty_gesture_result, 'shorthand and value properties should NOT have a value')
        self.assertTrue(empty_shorthand_result, 'shorthand property should NOT have a value')
        self.assertTrue(empty_value_result, 'value property should NOT have a value')

    def test_empty_if_false(self):

        gesture = KeyboardGesture(shorthand='x',
                                  value='x',
                                  date_created=datetime.today().strftime('%x %X %p'),
                                  date_updated=datetime.today().strftime('%x %X %p'))
        result = gesture.empty()
        self.assertFalse(result, 'shorthand and value properties should HAVE a value')

    def test_empty_return_type(self):

        gesture = KeyboardGesture(shorthand='',
                                  value='',
                                  date_created=datetime.today().strftime('%x %X %p'),
                                  date_updated=datetime.today().strftime('%x %X %p'))
        result = type(gesture.empty())
        self.assertEqual(bool, result, 'return type should be a <bool> type')
