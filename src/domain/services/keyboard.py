from src.domain.entities.keyboard import KeyboardGesture
from src.domain.repositories import keyboardGestureRepository
from src.gui.dialogs.messageboxes import WarningMessageBox


class KeyboardGestureService:

    def validateGesture(self, gesture: KeyboardGesture):

        validation = KeyboardGestureValidation()

        existing_gesture = keyboardGestureRepository.getGestureByShorthand(gesture)
        empty_gesture = gesture.empty()
        duplicate_gesture = gesture.duplicate(existing_gesture)

        if empty_gesture:
            empty_text = 'Shorthand and Value fields must not be empty.'
            validation.business_rules.append(empty_text)

        if duplicate_gesture:
            duplicate_text = 'Shorthand value already exist. Try entering a unique shorthand.'
            validation.business_rules.append(duplicate_text)

        validation.is_valid = not any([empty_gesture, duplicate_gesture])

        return validation


class KeyboardGestureValidation:

    is_valid = False
    business_rules = []
    messagebox = WarningMessageBox

    def __init__(self):

        self.business_rules.clear()

    def showError(self):

        self.messagebox.setText('Validation result')
        self.messagebox.setInformativeText('\n'.join(self.business_rules))
        self.messagebox.exec()
