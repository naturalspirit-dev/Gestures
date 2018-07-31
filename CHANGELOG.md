CHANGELOG
---------
All notable changes to this project will be documented on this file.

**Patch 1.2**

_Release date: 1 Sep 2018_

* What's new
    * Gestures and Meaning column can now be sorted

* Upgrade
    * Updated _keyboard_ 0.13.2
    * Updated _PyQt_ to 5.11.2
    * Updated _Python_ to 3.6.6

* Things to do
    - [x] QUESTION MARK: remove pyautogui implementation
    - [x] TOOLS: update to latest versions (keyboard, Python, PyQt)
    - [x] SHORTCUT: add 'Ctrl+Q' to quit the app 
    - [x] BUG: fix left alt value error
    - [ ] UI: make it run in the system tray
    - [ ] UI: find a suitable icon
    - [x] IMPROVEMENT: self.settings should be updated on the go
    - [ ] FEEDBACK: auto-sort when gestures are updated
    - [ ] REMOVE BUTTON: disable and enable when a gesture in the Gesture column is selected (2) should not ask what gesture to delete
    - [ ] REMOVE BUTTON: self-destruct when no existing gestures is remove  


**Patch 1.1.1**

_Release date: 2017-12-26_

* Bug fixes
    * Fixed a bug that enables the program to correctly 'typed' the question mark (?) character.
    * Fixed a bug that doesn't remove the _gesture_ after triggering it by a space.


**Patch 1.1**

_Release date: 2017-12-01_

* What's new
    * Restrict the user on entering existing gestures
    * Direct updating of _gesture_ and _meaning_ in the Gestures table
    * User can now open a website as gesture by simply adding its full URL 

* Upgrade
    * Python upgraded from Python 3.5.2 to **3.6.3**

* License
    * Added GNU GPL v3 as license for Gestures


**Patch 1.0**

_Release date: 2017-07-04_

* Features
    * User can now abbreviate commonly typed phrases such as passwords, emails, etc.
