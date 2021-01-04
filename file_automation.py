import os
import subprocess
import datetime

def note(text):
    """Creating a note
    Change the filepath into your dedicated filepath if intending of using this"""
    date = datetime.datetime.now()
    # changing the name of the file
    file_name = str(date).replace(":", "-") + " - note.txt"

    # checking for dedicated file path, make one if doesn't exist
    filepath = os.path.join("C:/Users/edwar/PycharmProjects/Jarvis/notes", file_name)
    if not os.path.exists("C:/Users/edwar/PycharmProjects/Jarvis/notes"):
        os.makedirs("C:/Users/edwar/PycharmProjects/Jarvis/notes")

    # make the note in the right directory
    with open(filepath, "w") as new_file:
        new_file.write(text)

    subprocess.Popen(["notepad.exe", filepath])