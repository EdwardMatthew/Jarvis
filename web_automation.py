from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import voice_functions as vf
import wikipedia


def play_youtube_vid():
    """Play the youtube video the user searched"""
    youtube_search = vf.take_command().lower().replace(" ", "+")

    # Initiate browser and maximize windows
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Wait until the web initializes and the elements are located and visible
    wait = WebDriverWait(driver, 5)
    visible = EC.visibility_of_element_located

    # Navigate to url
    driver.get(f"https://youtube.com/results?search_query={youtube_search}")

    # Detaching the browser from the code
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    # Play the video
    wait.until(visible((By.ID, "video-title")))
    videos = driver.find_elements_by_id("video-title")
    videos[0].click()

def search_google():
    """Searches google for the inquires"""
    google_search = vf.take_command().lower().replace(" ", "+") # replace function to fit the format of the query

    driver = webdriver.Chrome()
    driver.maximize_window()

    # Searching the input in google
    driver.get(f"https://google.com/search?q={google_search}")

    # Detaching the browser from the code
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

def search_wikipedia():
    """Getting the summary from wikipedia"""
    wikipedia_search = vf.take_command().lower()
    results = wikipedia.summary(wikipedia_search, sentences = 3)
    return results