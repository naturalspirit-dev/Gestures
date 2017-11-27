import keyboard as kb


# TEST: using keyboard.add_hotkey to execute a callable
def open_application():
    """ Using os.system """

    import os
    print('opening Notepad...')
    os.system(r'C:\Windows\notepad')

def open_application1():

    import subprocess
    subprocess.run([r'C:\Windows\notepad'])

def open_website():

    import webbrowser as wb
    wb.open_new_tab('https://www.python.org')


# If you want a shortcut type of gesture, use add_hotkey()
kb.add_hotkey('ctrl+alt+shift+x', open_application1)

# If you want a text type of gesture, use add_word_listener()
kb.add_word_listener("\'python", open_website)


class Gesture:

    def __init__(self):

        self.kind = 'core'

    def add_gesture(self, *args):

        pass

    def update_gesture(self, *args):

        pass

    def remove_gesture(self, *args):

        pass


class KeyboardGesture(Gesture):
    """ Currently handles abbreviation as gestures. """

    def __init__(self) -> None:

        super().__init__()
        self.kind = 'keyboard'

    def add_gesture(self, abbv: str, equiv: str) -> 'function':
        """ Add new gesture in the keyboard library. """

        return kb.add_abbreviation(abbv, equiv)

    def remove_gesture(self, abbv: str) -> dict:
        """ Remove existing gesture in the keyboard library. """

        return kb.remove_abbreviation(abbv)

