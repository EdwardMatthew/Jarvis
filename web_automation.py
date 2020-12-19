from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
import time


def play_youtube_vid():
    """Play the youtube video the user searched"""
    # Initiate browser and maximize windows
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Wait until the web initializes and the elements are located and visible
    wait = WebDriverWait(driver, 5)
    visible = EC.visibility_of_element_located

    # Navigate to url
    driver.get(f"https://youtube.com/results?search_query={youtube_search}")

    # Play the video
    wait.until(visible((By.ID, "video-title")))
    videos = driver.find_elements_by_id("video-title")
    videos[0].click()

    # Ensuring the video stays open
    while True:
        pass

def search_google():
    """Searches google for the inquires"""
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Searching the input in google
    driver.get(f"https://google.com/search?q={google_search}")

    # Ensuring the site stays open
    while True:
        pass

def send_email():











