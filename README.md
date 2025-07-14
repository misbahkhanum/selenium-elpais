# Selenium El País Scraper

## 🔍 Description
This project scrapes articles from the Opinion section of El País, translates the titles, analyzes repeated words, and runs tests on BrowserStack.

## 📁 Project Structure

- `scrape_articles.py` – Scrapes the first 5 opinion articles from El País.
- `translate_titles.py` – Translates article titles to English and analyzes word frequency.
- `browserstack_test.py` – Runs Selenium tests in 5 parallel threads on BrowserStack.
- `downloaded_images/` – Folder containing downloaded cover images.
- `requirements.txt` – Python dependencies.

## ▶️ How to Run

1. **Activate virtual environment**  
   ```bash
   .\venv\Scripts\activate
