# Core operations of Gestures

import keyboard as kb
from src.domain.entities.keyboard import KeyboardGesture


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


class KeyboardGestureLibrary:
    """ Core class that directly access the keyboard library APIs. """

    @staticmethod
    def addGesture(gesture: KeyboardGesture):
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(gesture.shorthand, gesture.value)

    @staticmethod
    def updateGesture(old_gesture: KeyboardGesture, new_gesture: KeyboardGesture):
        """ Remove old gesture and replace it by adding a new one to the keyboard library. """

        KeyboardGestureLibrary.removeGesture(old_gesture)
        KeyboardGestureLibrary.addGesture(new_gesture)

    @staticmethod
    def removeGesture(gesture: KeyboardGesture):
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(gesture.shorthand)
