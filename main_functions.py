import datetime
import pyjokes
import subprocess
import voice_functions as vf
import web_automation as wa
import greetings
import file_automation as fa
import textwrap
import webbrowser
import os
import winshell

def initialize_pickle():
    """Main engine"""
    try:
        # initializes the gmail api at the startup of the voice assistant
        service = wa.authenticate_gmail()

        # asking the user for their input
        vf.speak("how can I help you user?")

        # taking the voice input for running the functions
        command = vf.take_command().lower()


        if "play youtube" in command:
            vf.speak("what should I play?")
            query = vf.take_command().lower().replace(" ", "+")
            wa.play_youtube_vid(query)

        elif "how are you" in command:
            vf.speak("I am fine, thank you for asking!")

        elif "search google" in command:
            vf.speak("what would you like me to search?")
            query = vf.take_command().lower().replace(" ", "+")
            wa.search_google(query)

        elif "open google" in command:
            webbrowser.open("https://google.com")

        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%H : %M : %S")
            print(f"The time now is {time_now}")
            time_sound = str(time_now.split(":")[0])

            # Vars for the proper way of telling time
            time_hour = str(time_now.split(":")[0])
            time_minutes = str(time_now.split(":")[1])
            time_seconds = str(time_now.split(":")[2])

            # Checking for pm and am
            if int(time_sound) < 12:
                print(time_now)
                vf.speak(time_hour + "A M" + time_minutes + time_seconds)
            if int(time_sound) > 12:
                print(time_now)
                vf.speak(time_hour + "P M" + time_minutes + time_seconds)

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

        elif command == "restart system":
            vf.speak("are you sure you want to restart windows?")
            print("YES to restart and NO to cancel")
            restart = vf.take_command().lower()

            # Shutdown procedure
            if "YES" in restart:
                vf.speak("restarting the system, please wait a second...")
                subprocess.call(["shutdown", "/r"])
            if "NO" in restart:
                vf.speak("restart aborted. please continue with your work!")

        elif "wikipedia" in command:
            vf.speak("what does the user want to know?")
            wikipedia_search = vf.take_command().lower()
            search_results = wa.search_wikipedia(wikipedia_search)
            for words in textwrap.wrap(search_results, 80):
                print(words)
            vf.speak(f"according to wikipedia, {search_results}")

        elif "open outlook" in command:
            print("Opening Outlook...")
            vf.speak("opening outlook...")
            webbrowser.open("https://outlook.com")

        elif command == "make a note" or command == "write this down":
            vf.speak("what would you like me to note down?")
            new_note = vf.take_command().lower()
            if new_note != "cancel":
                fa.note(new_note)
                vf.speak("I've made a note for that")
                print("Note successfully made!")
            else:
                print("Cancelling...")
                vf.speak("process canceled")
                print("Cancelled")

        elif "empty recycle bin" in command:
            winshell.recycle_bin().empty(confirm=False, show_progress= False)
            vf.speak("recycle bin emptied!")
            print("the recycle bin is emptied!")

        elif command == "send an email":
            try:
                vf.speak("Okay, who would you like to send the email to?")

                # getting the email address of the recipient
                to_address = str(input("Please enter the email address of the recipient here"))

                # getting the message and the subject
                vf.speak("what should write?")
                content = vf.take_command()
                vf.speak("what should the subject be?")
                subject = vf.take_command()

                # Creating and sending the message
                msg = wa.create_message("me", to_address, subject, content)
                wa.send_message(service, "me", msg)
                vf.speak("I sent the email!")
            except Exception as e:
                print(e)
                vf.speak("I can't send this email, something's up.")
    except Exception as e:
        print(e)
        vf.speak("Something is not working properly. Please restart the initialization")
        quit()

WAKE = "hey pickle"

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    greetings.wish_me()
    USER = greetings.ask_for_name()
    if USER == None:
        vf.speak("username not recognized. The assistant will now shut down")
        print("Shutting down...")
        quit()

    else:
        initialize_pickle()

    # waking the VA
    while True:
        activate = vf.take_command().lower()
        if activate.count(WAKE) > 0:
            vf.speak("I am ready")
            initialize_pickle()
        elif activate.count("turn off") > 0:
            quit()
