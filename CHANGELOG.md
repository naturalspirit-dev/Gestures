CHANGELOG
---------
All notable changes to this project will be documented on this file.

**Patch 1.3**

_Release date: 6 Nov 2018 (tentative)_

* Things to do
    - [x] UI: make it run in the system tray


**Patch 1.2**

_Release date: 1 Sep 2018_

* What's new?
    * Gestures and Meaning column can now be sorted
    * _Remove_ button can now delete a selected gesture 

* UI
    * Added a shiny icon

* Bug Fixes
    * Fixed the 'left alt' ValueError 
    * Fixed a bug wherein updated gesture or meaning are not updated correctly
    * Fixed a bug wherein the user can still add an existing gesture

* Shortcut
    * Added 'Ctrl+Q' to quit the app

* Backend (the bloody part)
    * Remove usage of PyAutoGui which was a workaround for the '?' not typing properly
    * Settings are now updated for every add, update or remove  

* Upgrade
    * Updated _keyboard_ to 0.13.2
    * Updated _PyQt_ to 5.11.2
    * Updated _Python_ to 3.6.6


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
