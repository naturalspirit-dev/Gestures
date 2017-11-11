import keyboard as kb


class Gesture:

    def __init__(self):

        self.kind = 'core'

    def add_gesture(self, *args):

        pass

    def update_gesture(self, *args):

        pass

    def remove_gesture(self, *args):

        pass


class KeyboardGesture(Gesture):
    """ Currently handles abbreviation as gestures. """

    def __init__(self) -> None:

        super().__init__()
        self.kind = 'keyboard'

    def add_gesture(self, abbv: str, equiv: str) -> 'function':
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(abbv, equiv)

    def remove_gesture(self, abbv: str) -> dict:
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(abbv)
