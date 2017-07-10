import keyboard as kb


class Gestures:

    def __init__(self):
        self.__version__ = '1.1'
        self.abbv = ''
        self.equivalent = ''
        self.gestures = {}
        self.read_gestures_from_file('shortcuts.txt')

    def add_gesture(self, abbv: str, equivalent: str) -> None:
        """ Register new gesture based on user's input. """

        self.gestures[abbv] = equivalent

    # TODO: review if you still need this
    def get_raw_gesture(self, raw_abbv: str, raw_equivalent: str) -> dict:
        """ Return gestures based on user's input. """

        self.abbv = raw_abbv
        self.equivalent = raw_equivalent
        return {self.abbv: self.equivalent}

    def show_gestures(self) -> None:
        """ Display current list of gestures. """

        sorted_AZ = sorted(self.gestures.items())
        print('count -> {}'.format(len(sorted_AZ)))
        for k, v in sorted_AZ:
            print('{0:<15s}: {1}'.format(k, v))

    def add_gesture_to_keyboard(self) -> None:
        """ Register new gesture to keyboard library. """

        if self.validate_user_input():
            kb.add_abbreviation(self.abbv, self.equivalent)
            self.add_gesture(self.abbv, self.equivalent)
            self.write_gestures_to_file(self.abbv, self.equivalent)

    def validate_user_input(self) -> bool:
        """ Return True if user's input passes all validations. """

        argument_type = self.check_argument_type(self.abbv, self.equivalent)
        unique_gesture = self.check_unique_gesture(self.abbv)

        return argument_type and unique_gesture

    def check_argument_type(self, abbv: str, equivalent: str) -> bool:
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

    def write_gestures_to_file(self, abbv: str, equiv: str) -> bool:
        """ Write registered gesture into a text file named shortcuts.txt. """

        with open('shortcuts.txt', 'a') as gestures_file:
            gestures_file.write('{0:<15s}: {1}\n'.format(abbv, equiv))
            return True

    # TODO: for testing
    def read_gestures_from_file(self, filename: str):
        """ Retrieved and load saved gestures from a text file. 
            
            Load saved shortcuts to keyboard.    
        """

        # TODO: retrieved shortcuts.txt
        with open(filename) as gestures_file:
            for line in gestures_file:
                separate = line.split(':')
                abbv = separate[0].rstrip()
                equiv = separate[1].lstrip().strip('\n')
                self.abbv = abbv
                self.equivalent = equiv
                self.add_gesture_to_keyboard()
        return True

