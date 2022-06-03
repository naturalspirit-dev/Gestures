# Core operations of Gestures

import keyboard as kb
from src.domain.entities.keyboard_gesture import KeyboardGesture as KeyboardGestureEntity


class Gesture:
    """ The core of the cores. """

    def __init__(self):

        self.kind = 'core'

    def add_gesture(self, *args):

        pass

    def update_gesture(self, *args):

        pass

    def remove_gesture(self, *args):

        pass


class KeyboardGesture(Gesture):
    """ Core class that directly access the keyboard library APIs. """

    def __init__(self) -> None:

        super().__init__()
        self.kind = 'keyboard'

    def add_gesture(self, gesture: str, meaning: str) -> 'function':
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(gesture, meaning)

    def update_gesture(self, old_gesture: list, new_gesture: KeyboardGestureEntity):
        """ Remove old gesture and add a new one to the keyboard library. """

        self.remove_gesture(old_gesture[0])
        self.add_gesture(new_gesture.shorthand, new_gesture.value)

    def remove_gesture(self, gesture: str) -> dict:
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(gesture)
