from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from googletrans import Translator

# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://elpais.com/")

# Get page title
title = driver.title
print("Title:", title)

# Translate title
translator = Translator()
translated = translator.translate(title, src='es', dest='en')
print("Translated Title:", translated.text)

driver.quit()

