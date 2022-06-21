from __future__ import annotations
from datetime import datetime


class KeyboardGesture:
    id = int
    shorthand = str
    value = str
    date_created = datetime
    date_updated = datetime

    def __init__(self, id=None, shorthand='', value='', date_created=datetime, date_updated=datetime):

        self.id = id
        self.shorthand = shorthand
        self.value = value
        self.date_created = date_created
        self.date_updated = date_updated

    @property
    def values(self):

        return [self.id, self.shorthand, self.value, self.date_created, self.date_updated]

    # Business rules
    def empty(self) -> bool:

        return not all([self.shorthand, self.value])

    def duplicate(self, gesture: KeyboardGesture) -> bool:

        if gesture:
            return self.shorthand == gesture.shorthand
        else:
            return False
