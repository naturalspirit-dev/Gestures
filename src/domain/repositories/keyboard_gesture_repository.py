from src.core.gestures import KeyboardGesture as KeyboardGestureCore
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.infrastructure.database import GesturesDatabase


class KeyboardGestureRepository:

    def __init__(self):

        self.keyboardGestureList = []
        self.keyboard_core = KeyboardGestureCore()      # keyboard library storage
        self.gestures_database = GesturesDatabase()     # database storage
        self.initializeKeyboardCore()

    def initializeKeyboardCore(self):

        records = self.getAllGestures()
        self.keyboardGestureList = records
        for record in records:
            self.keyboard_core.add_gesture(record[0], record[1])

    def addRecord(self, gestures: KeyboardGesture):

        record = [gestures.shorthand, gestures.value]

        self.gestures_database.addGesture(gestures)
        self.keyboard_core.add_gesture(gestures.shorthand, gestures.value)
        self.keyboardGestureList.append(record)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        old_record = self.keyboardGestureList[index]
        new_record = [gesture.shorthand, gesture.value]
        self.keyboardGestureList[index] = new_record
        self.keyboard_core.update_gesture(old_record, gesture)

    def removeRecord(self, index: int):

        existing_record = self.keyboardGestureList.pop(index)
        self.keyboard_core.remove_gesture(existing_record[0])

    def count(self):

        return len(self.keyboardGestureList)

    def getAllGestures(self):

        records = self.gestures_database.getAllGestures()
        gestures = [list(record) for record in records]

        return gestures
