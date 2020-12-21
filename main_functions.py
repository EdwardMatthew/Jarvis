import pyttsx3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import datetime
import time
import voice_functions as vf
import web_automation as wa
import greetings as greetings

def initialize_mustard():
    greetings.wish_me()
    greetings.ask_for_name()

    while True:
        """Looping the engine"""
        command = vf.take_command().lower()

        if "play a youtube video" in command:
            vf.speak("what should I play?")
            wa.play_youtube_vid()

        elif "how are you" in command:
            vf.speak("I am fine, thank you for asking!")

        elif "search google" in command:
            vf.speak("what would you like me to search?")
            wa.search_google()

        elif "the time" or "what time is it" in command:
            time_now = datetime.datetime.now().strftime("%H : %M : %S")
            print(time_now)
            vf.speak(f"the time is {time_now}")

        elif "thanks mustard" or "thank you mustard" in command:
            vf.speak("shutting down...")
            print("Shutting down...")
            exit()

initialize_mustard()