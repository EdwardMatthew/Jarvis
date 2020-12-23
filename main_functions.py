import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import time
import pyjokes
import wikipedia
import subprocess
import voice_functions as vf
import web_automation as wa
import greetings as greetings
import files
import shutil
import pprint

def initialize_mustard():
    greetings.wish_me()
    greetings.ask_for_name()

    active = True

    while active:
        """Looping the engine"""
        command = vf.take_command().lower()

        if "play youtube" in command:
            vf.speak("what should I play?")
            wa.play_youtube_vid()

        elif "how are you" in command:
            vf.speak("I am fine, thank you for asking!")

        elif "search google" in command:
            vf.speak("what would you like me to search?")
            wa.search_google()

        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%H : %M : %S")
            print(time_now)
            vf.speak(f"the time now is {time_now}")

        elif "joke" in command:
            vf.speak(pyjokes.get_joke())

        elif "good morning" in command:
            vf.speak("good morning user! have a great day!")

        elif command == "shutdown system":
            vf.speak("are you sure you want to shutdown windows?")
            print("YES to shutdown and NO to cancel")
            shut_down = vf.take_command().lower()

            # Shutdown procedure
            if "YES" in shut_down:
                vf.speak("Shutting down the system, please wait a second...")
                subprocess.call("shutdown / p / f")
            if "NO" in shut_down:
                vf.speak("shutdown aborted. please continue with your work!")

        elif "wikipedia" in command:
            vf.speak("what does the user want to know?")
            search_results = wa.search_wikipedia()
            pp = pprint.PrettyPrinter(width=78, compact=True)
            pp.pprint(search_results)
            vf.speak(f"According to wikipedia, {search_results}")

        elif command == "make a note" or command == "write this down":
            vf.speak("what would you like me to note down?")
            new_note = vf.take_command().lower()
            if new_note != "cancel":
                files.note(new_note)
                vf.speak("I've made a note for that")
                print("Note successfully made!")
            else:
                quit(files.note)

        elif "I'm done" or "Thank you" in command:
            print("Shutting down...")
            vf.speak("shutting down...")
            exit()

        else:
            vf.speak("command not recognized. Please try again")

initialize_mustard()