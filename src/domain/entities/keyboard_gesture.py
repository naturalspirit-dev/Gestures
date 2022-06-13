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
        self.date_created = datetime.today().strftime('%x %X %p')
        self.date_updated = datetime.today().strftime('%x %X %p')

    # Business rules
    def empty(self):

        return not all([self.shorthand, self.value])

    # [] TODO: no duplicate shorthands
