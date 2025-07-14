from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# Set up folder
if not os.path.exists("downloaded_images"):
    os.makedirs("downloaded_images")

driver = webdriver.Chrome()
driver.get("https://elpais.com/")
time.sleep(5)

# Navigate to the Opinion section
opinion_link = driver.find_element(By.LINK_TEXT, "Opinión")
opinion_link.click()
time.sleep(5)

# Find the first 5 articles
articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]

for idx, article in enumerate(articles):
    try:
        title = article.find_element(By.TAG_NAME, "h2").text
        print(f"\nTitle {idx+1}: {title}")

        article.find_element(By.TAG_NAME, "a").click()
        time.sleep(5)

        content = driver.find_element(By.CSS_SELECTOR, "div.articulo-cuerpo").text
        print(f"Content:\n{content[:300]}...\n")

        # Try to get the image
        try:
            image = driver.find_element(By.CSS_SELECTOR, "figure img")
            image_url = image.get_attribute("src")
            print("Found image URL:", image_url)

            img_data = requests.get(image_url).content
            with open(f"downloaded_images/article_{idx+1}.jpg", 'wb') as f:
                f.write(img_data)
            print("✅ Image saved!")

        except Exception as img_err:
            print("❌ No image found:", img_err)

        driver.back()
        time.sleep(3)
        articles = driver.find_elements(By.CSS_SELECTOR, "article")[:5]  # Refresh list

    except Exception as e:
        print("❌ Error processing article:", e)

driver.quit()
