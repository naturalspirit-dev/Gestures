

class KeyboardGesture:
    type = str
    shorthand = str
    value = str

    def __init__(self, shorthand='', value=''):

        self.shorthand = shorthand
        self.value = value
