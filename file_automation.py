import os
import subprocess
import datetime
import voice_functions as vf

def note(text):
    """Creating a note"""
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + " - note.txt" # changing the naming convention to proper format
    with open(file_name, "w") as new_file:
        new_file.write(text)

    subprocess.Popen(["notepad.exe", file_name])