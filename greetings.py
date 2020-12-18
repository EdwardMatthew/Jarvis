import voice_functions as vf
import datetime
import pyttsx3
import shutil


def wish_me():
    """Greet user based on time"""
    hour = int(datetime.datetime.now().hour)
    if 12 > hour > 0:
        vf.speak("Good morning user!")
    elif 18 > hour > 12:
        vf.speak("Good afternoon user!")
    else:
        vf.speak("Good evening user!")

def ask_for_name():
    """Asking user on what to call them"""
    vf.speak("What should I call you user?")
    user_name = vf.take_command()

    # Get columns
    columns = shutil.get_terminal_size().columns

    try:
        print("#####################".center(columns))
        print(f"Welcome, {user_name.center(columns)}")
        vf.speak(f"Welcome, {user_name}")
        print("#####################".center(columns))

    except Exception as e:
        print("Name not recognized.")
        vf.speak("Name not recognized")
        return None

ask_for_name()