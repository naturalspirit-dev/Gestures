from __future__ import annotations
from typing import Optional
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

    def duplicate(self, existing_gesture: KeyboardGesture | None, selected_gesture: KeyboardGesture | None = None) -> bool:

        if existing_gesture:
            if selected_gesture:
                if selected_gesture.shorthand != existing_gesture.shorthand:
                    return self.shorthand == existing_gesture.shorthand
                else:
                    return False
            else:
                return self.shorthand == existing_gesture.shorthand
        else:
            return False
