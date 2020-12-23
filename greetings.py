import datetime
import voice_functions as vf

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

    # getting name from user
    try:
        vf.speak(f"Welcome {user_name}")
        print(f"Username : {user_name}")
        vf.speak("how can I help you sir?")
        return user_name

    except Exception as e:
        print(e)
        vf.speak("Name not recognized. Shutting down...")
        return None
