from src.domain.repositories.keyboard_gesture_repository import *


class KeyboardGestureService:

    def create(self, keyboard_gesture: KeyboardGesture):

        print('add to keyboard library', keyboard_gesture)
