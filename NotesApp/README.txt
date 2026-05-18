NotesApp
========
A local Apple Notes-style app that runs in your browser.
Notes are stored as .json files in the notes/ folder — they persist
across browser sessions, incognito windows, and browser data clears.


REQUIREMENTS
------------
• Python 3.7 or later  (https://www.python.org/downloads/)
• pip  (included with Python 3)


INSTALLATION & RUNNING
----------------------

Option A — Terminal (simplest)
  1. Open Terminal and navigate to this folder:
       cd ~/Desktop/NotesApp
  2. Install Flask (one-time):
       pip3 install -r requirements.txt
  3. Start the app:
       python3 app.py
  The browser opens automatically at http://127.0.0.1:5000

Option B — Double-click on Mac
  1. Open Terminal and make run.sh executable (one-time step):
       chmod +x ~/Desktop/NotesApp/run.sh
  2. In Finder, right-click run.sh → Open With → Terminal
     (First time only — macOS will ask you to confirm opening it.)
  After that first time, you can double-click run.sh to launch.

  Tip: rename run.sh to run.command and it will open in Terminal
  automatically on double-click without the right-click step.


FEATURES
--------
• Create, edit, and delete notes
• Auto-save 600 ms after you stop typing
• Rich text: Bold (⌘B), Italic (⌘I), Underline (⌘U),
  H1, H2, bullet lists, numbered lists
• Search notes by title or body text (Esc to clear)
• New note shortcut: ⌘N
• Resizable sidebar (drag the divider)
• Live word count and timestamps


WHERE NOTES ARE STORED
----------------------
  ~/Desktop/NotesApp/notes/<uuid>.json

Each file is a plain JSON object with id, title, body (HTML),
created_at, and updated_at. You can back them up, sync them with
Dropbox/iCloud Drive, or read them with any text editor.


STOPPING THE SERVER
-------------------
Press Ctrl+C in the Terminal window where the app is running.
