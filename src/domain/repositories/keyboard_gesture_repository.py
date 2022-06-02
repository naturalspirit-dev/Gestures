from src.core.gestures import KeyboardGesture as Kb
from src.domain.entities.keyboard_gesture import KeyboardGesture


class KeyboardGestureRepository:

    def __init__(self):

        self.keyboardGestureList = []
        self.kb = Kb()

    def addRecord(self, gestures: KeyboardGesture):

        record = [gestures.shorthand, gestures.value]
        self.keyboardGestureList.append(record)
        self.kb.add_gesture(gestures.shorthand, gestures.value)

    def updateRecord(self, index: int, gesture: KeyboardGesture):

        record = [gesture.shorthand, gesture.value]
        self.keyboardGestureList[index] = record

    def removeRecord(self, index: int):

        del self.keyboardGestureList[index]

    def count(self):

        return len(self.keyboardGestureList)
