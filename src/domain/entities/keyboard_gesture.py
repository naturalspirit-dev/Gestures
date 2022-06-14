from datetime import datetime


class KeyboardGesture:
    id = int
    shorthand = str
    value = str
    date_created = datetime
    date_updated = datetime

    def __init__(self, shorthand='', value=''):

        self.shorthand = shorthand
        self.value = value

    @property
    def values(self):

        return [self.id, self.shorthand, self.value, self.date_created, self.date_updated]

    # Business rules
    def empty(self):

        return not all([self.shorthand, self.value])

    # [] TODO: no duplicate shorthands
