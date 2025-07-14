from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import time

# Set up Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to El País Opinion section
driver.get("https://elpais.com/opinion/")
time.sleep(5)  # Let page load

# Create folder for images if it doesn't exist
if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

# Find top 5 opinion articles
articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]

for idx, article in enumerate(articles):
    try:
        # Click to go to article page
        link = article.find_element(By.TAG_NAME, "a").get_attribute("href")
        driver.get(link)
        time.sleep(4)

        # Extract title
        title = driver.find_element(By.TAG_NAME, "h1").text
        print(f"\nTitle {idx+1}: {title}")

        # Extract content
        paragraphs = driver.find_elements(By.CSS_SELECTOR, "div.a_c p")
        content = "\n".join(p.text for p in paragraphs if p.text.strip())
        print(f"Content (first 300 chars):\n{content[:300]}...\n")

        # Try downloading the main image
        try:
            image_element = driver.find_element(By.CSS_SELECTOR, "picture img")
            image_url = image_element.get_attribute("src")
            if image_url:
                response = requests.get(image_url)
                image_filename = os.path.join("downloaded_images", f"article_{idx+1}.jpg")
                with open(image_filename, "wb") as f:
                    f.write(response.content)
                print(f"✅ Image downloaded: {image_filename}")
        except Exception as img_error:
            print(f"⚠️ No image found or failed to download: {img_error}")

    except Exception as e:
        print(f"❌ Error processing article {idx+1}: {e}")

    # Go back to the main page
    driver.get("https://elpais.com/opinion/")
    time.sleep(3)

driver.quit()
