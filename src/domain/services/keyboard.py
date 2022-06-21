from src.domain.entities.keyboard import KeyboardGesture
from src.domain.repositories import keyboardGestureRepository


class KeyboardGestureService:

    def isValid(self, gesture: KeyboardGesture):

        existing_gesture = keyboardGestureRepository.getGestureByShorthand(gesture)
        empty_gesture = gesture.empty()
        duplicate_gesture = gesture.duplicate(existing_gesture)

        return not any([empty_gesture, duplicate_gesture])
