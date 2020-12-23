import pyttsx3
import speech_recognition as sr

# Initialize text to speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# Voice engine, change the index to 1 for female voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Get command from user"""
    r = sr.Recognizer()

    # set up microphone to take user command
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        # error handling
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language="en-GB")
            print(f"User said : {command}")

        except Exception as e:
            print(e)
            speak("Voice not recognized.")
            return None

    return command