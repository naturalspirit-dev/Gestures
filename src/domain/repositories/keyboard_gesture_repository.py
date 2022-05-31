from src.domain.entities.keyboard_gesture import KeyboardGesture


class KeyboardGestureRepository:

    def __init__(self):

        self.keyboardGestureList = []

    def addRecord(self, keyboard_gesture: KeyboardGesture):

        record = [keyboard_gesture.shorthand, keyboard_gesture.value]
        self.keyboardGestureList.append(record)

    def removeRecord(self, index: int):

        del self.keyboardGestureList[index]
