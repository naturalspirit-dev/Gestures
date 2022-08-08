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

    def test_empty_return_type_if_bool(self):

        gesture = KeyboardGesture(shorthand='',
                                  value='',
                                  date_created=datetime.today().strftime('%x %X %p'),
                                  date_updated=datetime.today().strftime('%x %X %p'))
        result = type(gesture.empty())
        self.assertEqual(bool, result, 'return type should be a <bool> type')

    def test_duplicate_on_create_if_true(self):

        original_gesture = KeyboardGesture(shorthand='original',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        duplicate_gesture = KeyboardGesture(shorthand='original',
                                            value='gesture',
                                            date_created=datetime.today().strftime('%x %X %p'),
                                            date_updated=datetime.today().strftime('%x %X %p'))

        result = original_gesture.duplicate(duplicate_gesture)
        self.assertTrue(result, 'shorthand property should be equal')

    def test_duplicate_on_create_if_false(self):

        original_gesture = KeyboardGesture(shorthand='original',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        different_gesture = KeyboardGesture(shorthand='different',
                                            value='gesture',
                                            date_created=datetime.today().strftime('%x %X %p'),
                                            date_updated=datetime.today().strftime('%x %X %p'))

        result = original_gesture.duplicate(different_gesture)
        self.assertFalse(result, 'shorthand property should NOT be equal')

    def test_duplicate_on_update_if_true(self):

        new_gesture = KeyboardGesture(shorthand='existing',
                                      value='gesture',
                                      date_created=datetime.today().strftime('%x %X %p'),
                                      date_updated=datetime.today().strftime('%x %X %p'))

        selected_gesture = KeyboardGesture(shorthand='selected',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        existing_gesture = KeyboardGesture(shorthand='existing',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        result = new_gesture.duplicate(existing_gesture, selected_gesture)
        self.assertTrue(result, "new_gesture's shorthand property should be equal to existing_gesture's shorthand property")

    def test_duplicate_on_update_if_false(self):

        new_gesture = KeyboardGesture(shorthand='existing',
                                      value='gesture',
                                      date_created=datetime.today().strftime('%x %X %p'),
                                      date_updated=datetime.today().strftime('%x %X %p'))

        selected_gesture = KeyboardGesture(shorthand='selected',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        existing_gesture = KeyboardGesture(shorthand='not found',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        result = new_gesture.duplicate(existing_gesture, selected_gesture)
        self.assertFalse(result, "new_gesture's shorthand property should NOT be equal to existing_gesture's shorthand property")

    def test_duplicate_on_update_if_false_if_updating_itself(self):

        new_gesture = KeyboardGesture(shorthand='selected',
                                      value='new value',
                                      date_created=datetime.today().strftime('%x %X %p'),
                                      date_updated=datetime.today().strftime('%x %X %p'))

        selected_gesture = KeyboardGesture(shorthand='selected',
                                           value='old value',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        existing_gesture = KeyboardGesture(shorthand='not found',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        result = new_gesture.duplicate(existing_gesture, selected_gesture)
        self.assertFalse(result, "new_gesture's shorthand property should be equal to selected_gesture's shorthand property")

    def test_duplicate_return_type_if_bool(self):

        original_gesture = KeyboardGesture(shorthand='original',
                                           value='gesture',
                                           date_created=datetime.today().strftime('%x %X %p'),
                                           date_updated=datetime.today().strftime('%x %X %p'))

        duplicate_gesture = KeyboardGesture(shorthand='original',
                                            value='gesture',
                                            date_created=datetime.today().strftime('%x %X %p'),
                                            date_updated=datetime.today().strftime('%x %X %p'))

        result = type(original_gesture.duplicate(duplicate_gesture))
        self.assertEqual(bool, result, 'return type should be a <bool> type')
