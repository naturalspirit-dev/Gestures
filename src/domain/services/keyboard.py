from PyQt5.QtCore import QModelIndex
from src.domain.entities.keyboard import KeyboardGesture
from src.domain.repositories import keyboardGestureRepository
from src.gui.dialogs.messageboxes import WarningMessageBox


class KeyboardGestureService:

    def validateGesture(self, gesture: KeyboardGesture):

        existing_gesture = keyboardGestureRepository.getGestureByShorthand(gesture)

        empty_gesture = gesture.empty()
        duplicate_gesture = gesture.duplicate(existing_gesture)

        return self.validate(empty_gesture, duplicate_gesture)

    def validateGestureOnUpdate(self, selected_index: QModelIndex, updated_gesture: KeyboardGesture):

        selected_gesture = KeyboardGesture(shorthand=selected_index.sibling(selected_index.row(), 1).data())
        existing_gesture = keyboardGestureRepository.getGestureByShorthand(updated_gesture)

        empty_gesture = updated_gesture.empty()
        duplicate_gesture = updated_gesture.duplicate(existing_gesture, selected_gesture)

        return self.validate(empty_gesture, duplicate_gesture)

    def validate(self, empty: bool, duplicate: bool):

        validation = KeyboardGestureValidation()

        if empty:
            empty_text = 'Shorthand and Value fields must not be empty.'
            validation.business_rules.append(empty_text)

        if duplicate:
            duplicate_text = 'Shorthand value already exist. Try entering a unique shorthand.'
            validation.business_rules.append(duplicate_text)

        validation.is_valid = not any([empty, duplicate])

        return validation

    def validateSelectedIndex(self, selected_index: QModelIndex, action: str):

        validation = KeyboardGestureValidation()

        if selected_index.isValid():
            validation.is_valid = True
        else:
            no_selected_text = f'Please select a record in the table that you want to {action}.'
            validation.business_rules.append(no_selected_text)
            validation.is_valid = False

        return validation

    def getTotalRecords(self):

        return keyboardGestureRepository.count()


class KeyboardGestureValidation:

    is_valid = False
    business_rules = []
    messagebox = WarningMessageBox

    def __init__(self):

        self.business_rules.clear()

    def showValidationDialog(self):

        self.messagebox.setText('Validation result')
        self.messagebox.setInformativeText('\n'.join(self.business_rules))
        self.messagebox.exec()
