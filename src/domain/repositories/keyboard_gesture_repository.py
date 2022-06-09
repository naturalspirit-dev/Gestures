from src.core.gestures import KeyboardGesture as KeyboardGestureCore
from src.domain.entities.keyboard_gesture import KeyboardGesture
from src.infrastructure.database import GesturesDatabase


class KeyboardGestureRepository:

    def __init__(self):

        self.keyboardGestureList = []
        self.kb = KeyboardGestureCore()                 # keyboard library storage
        self.gestures_database = GesturesDatabase()     # database storage

    def addRecord(self, gestures: KeyboardGesture):

        record = [gestures.shorthand, gestures.value]

        self.gestures_database.addGesture(gestures)
        self.kb.add_gesture(gestures.shorthand, gestures.value)
        self.keyboardGestureList.append(record)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        old_record = self.keyboardGestureList[index]
        new_record = [gesture.shorthand, gesture.value]
        self.keyboardGestureList[index] = new_record
        self.kb.update_gesture(old_record, gesture)

    def removeRecord(self, index: int):

        existing_record = self.keyboardGestureList.pop(index)
        self.kb.remove_gesture(existing_record[0])

    def count(self):

        return len(self.keyboardGestureList)

    def getAllGestures(self):

        gestures = self.gestures_database.getAllGestures()
        for gesture in gestures:
            print(gesture)
