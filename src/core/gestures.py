# Core operations of Gestures

import keyboard as kb
from src.domain.entities.keyboard_gesture import KeyboardGesture as KeyboardGestureEntity


class Gesture:
    """ The core of the cores. """

    def __init__(self):

        self.kind = 'core'

    def addGesture(self, *args):

        pass

    def updateGesture(self, *args):

        pass

    def removeGesture(self, *args):

        pass


class KeyboardGesture(Gesture):
    """ Core class that directly access the keyboard library APIs. """

    def __init__(self):

        super().__init__()
        self.kind = 'keyboard'

    def addGesture(self, gesture: KeyboardGestureEntity) -> 'function':
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(gesture.shorthand, gesture.value)

    def updateGesture(self, old_gesture: KeyboardGestureEntity, new_gesture: KeyboardGestureEntity):
        """ Remove old gesture and replace it by adding a new one to the keyboard library. """

        self.removeGesture(old_gesture)
        self.addGesture(new_gesture)

    def removeGesture(self, gesture: KeyboardGestureEntity) -> dict:
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(gesture.shorthand)
