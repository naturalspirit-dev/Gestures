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

        self.keyboardGestureList = self.getAllGestures()
        for gesture in self.keyboardGestureList:
            self.keyboard_core.add_gesture(gesture.shorthand, gesture.value)

    def addRecord(self, gesture: KeyboardGesture):

        new_record = self.gestures_database.addGesture(gesture)
        self.keyboardGestureList.append(new_record.values)
        self.keyboard_core.add_gesture(new_record.shorthand, new_record.value)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        old_record = self.keyboardGestureList[index]
        new_record = [
            old_record[0],          # id
            gesture.shorthand,
            gesture.value,
            old_record[3],          # date_created
            gesture.date_updated
        ]
        gesture.id = old_record[0]
        gesture.date_created = old_record[3]

        self.keyboardGestureList[index] = new_record
        self.gestures_database.updateGesture(gesture)
        self.keyboard_core.update_gesture(old_record, gesture)

    def removeRecord(self, index: int):

        existing_record = self.keyboardGestureList.pop(index)
        self.gestures_database.removeGesture(existing_record[0])
        self.keyboard_core.remove_gesture(existing_record[1])

    def count(self):

        return len(self.keyboardGestureList)

    def getAllGestures(self):

        records = self.gestures_database.getAllGestures()

        gestures_list = []
        for record in records:
            gesture = KeyboardGesture()
            gesture.id = record[0]
            gesture.shorthand = record[1]
            gesture.value = record[2]
            gesture.date_created = record[3]
            gesture.date_updated = record[4]
            gestures_list.append(gesture)

        return gestures_list
