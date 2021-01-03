from __future__ import print_function
import mimetypes
import pickle
import os.path
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

import wikipedia
import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def play_youtube_vid(youtube_query):
    """Play the youtube video the user searched"""
    # Initiate browser and maximize windows
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Wait until the web initializes and the elements are located and visible
    wait = WebDriverWait(driver, 5)
    visible = EC.visibility_of_element_located

    # Navigate to url
    driver.get(f"https://youtube.com/results?search_query={youtube_query}")

    # Detaching the browser from the code
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Play the video
    wait.until(visible((By.ID, "video-title")))
    videos = driver.find_elements_by_id("video-title")
    videos[0].click()

def search_google(google_query):
    """Searches google for the inquires"""
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Searching the input in google
    driver.get(f"https://google.com/search?q={google_query}")

    # Detaching the browser from the code
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

def search_wikipedia():
    """Getting the summary from wikipedia"""
    wikipedia_search = vf.take_command().lower()
    results = wikipedia.summary(wikipedia_search, sentences = 3)
    return results


SCOPES = ['https://mail.google.com/']

def authenticate_gmail():
    """Authenticates the gmail api service"""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service

def create_message(sender, to, subject, message_text):
    """Create a message without attachments"""
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {"raw" : base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id, message):
    """Send an email"""
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print("Message Id : %s" %message["id"])
    except HttpError as error:
        print("An error occured : %s" %error)
