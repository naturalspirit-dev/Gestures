# Project Structure

The current project and sub-folder is organized as follows:
```
Gestures
    + docs .......................................... documentations
    + images ........................................ JPEG files
    + gestures ...................................... source code
        + domain
            + entities .............................. models
            + services .............................. things to do about your entities
            + repositories .......................... CRUD
        + core ...................................... controller between your domain and gui
        + gui ....................................... front-end
            + dialogs ............................... sub-windows and dialogs
            + widgets ............................... UI controls like buttons, textboxes, etc.
            + windows ............................... main window
    + tests ......................................... unit tests
```
