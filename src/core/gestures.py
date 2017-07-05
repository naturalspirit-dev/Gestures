import keyboard as kb


class Gestures:

    def __init__(self):
        self.__version__ = '1.1'
        self.abbv = ''
        self.equivalent = ''
        self.gestures = {}

    # TODO: for testing
    def add_gesture(self, abbv: str, equivalent: str) -> None:
        """ Register new gesture based on user's input. """

        self.gestures[abbv] = equivalent

    # TODO: review if you still need this
    def get_gestures(self, abbv, equivalent) -> dict:
        """ Return gestures based on user's input. """

        self.abbv = abbv
        self.equivalent = equivalent
        return {self.abbv: self.equivalent}

    def show_gestures(self) -> None:
        """ Display current list of gestures. """

        sorted_AZ = sorted(self.gestures.items())
        print('count -> {}'.format(len(sorted_AZ)))
        for k, v in sorted_AZ:
            print('{0}: {1}'.format(k, v))

    def add_gesture_to_keyboard(self) -> None:
        """ Register new gesture to keyboard library. """

        if self.validate_user_input():
            kb.add_abbreviation(self.abbv, self.equivalent)
            self.add_gesture(self.abbv, self.equivalent)

    def validate_user_input(self) -> bool:
        """ Return True if user's input passes all validations. """

        argument_type = self.check_argument_type(self.abbv, self.equivalent)
        unique_gesture = self.check_unique_gesture(self.abbv)

        return argument_type and unique_gesture

    def check_argument_type(self, abbv, equivalent):
        """ Return True if self.abbv and self.equivalent are both str type. """

        if isinstance(abbv, str) and isinstance(equivalent, str):
            return True
        else:
            return False

    def check_unique_gesture(self, abbv: str) -> bool:
        """ Return True if abbv is unique (no duplicate) else return False. """

        if abbv not in kb._word_listeners.keys():
            return True
        else:
            print('\'{}\' already exist.'.format(abbv))
            return False