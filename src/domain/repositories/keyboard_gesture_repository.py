from src.core.gestures import KeyboardGestureLibrary
from src.domain.entities.keyboard import KeyboardGesture
from src.infrastructure.database import GesturesDatabase


class KeyboardGestureRepository:

    def __init__(self):

        self.keyboardGestureList = []
        self.gestures_database = GesturesDatabase()         # database storage
        self.initializeKeyboardCore()

    def initializeKeyboardCore(self):

        self.keyboardGestureList = self.getAllGestures()
        for gesture in self.keyboardGestureList:
            KeyboardGestureLibrary.addGesture(gesture)

    def addRecord(self, gesture: KeyboardGesture):

        new_gesture = self.gestures_database.addGesture(gesture)
        self.keyboardGestureList.append(new_gesture)
        KeyboardGestureLibrary.addGesture(gesture)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        old_gesture = self.keyboardGestureList[index]
        updated_gesture = KeyboardGesture(id=old_gesture.id,
                                          shorthand=gesture.shorthand,
                                          value=gesture.value,
                                          date_created=old_gesture.date_created,
                                          date_updated=gesture.date_updated)
        self.keyboardGestureList[index] = updated_gesture
        self.gestures_database.updateGesture(updated_gesture)
        KeyboardGestureLibrary.updateGesture(old_gesture, updated_gesture)

    def removeRecord(self, index: int):

        existing_record = self.keyboardGestureList.pop(index)
        self.gestures_database.removeGesture(existing_record)
        KeyboardGestureLibrary.removeGesture(existing_record)

    def count(self):

        return len(self.keyboardGestureList)

    def getAllGestures(self):

        return self.gestures_database.getAllGestures()

    def getGestureByShorthand(self, gesture: KeyboardGesture):

        return self.gestures_database.getGestureByShorthand(gesture)
