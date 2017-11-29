# Core operations of Gestures

import keyboard as kb


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
    """ Currently handles abbreviation and opening of website as gestures. """

    def __init__(self) -> None:

        super().__init__()
        self.kind = 'keyboard'

    def add_gesture(self, gesture: str, meaning: str) -> 'function':
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(gesture, meaning)

    def remove_gesture(self, gesture: str) -> dict:
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(gesture)

