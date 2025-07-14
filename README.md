# 📰 Selenium El País Scraper

## 🔍 Description
This project scrapes articles from the **Opinion** section of [El País](https://elpais.com/), translates the titles to English, analyzes repeated words, and runs automated Selenium tests on BrowserStack.

---

## 📁 Project Structure

| File/Folder              | Purpose                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| `elpais_opinion_scraper.py` | Scrapes the first 5 opinion articles from El País                      |
| `translate_titles.py`       | Translates article titles and performs word frequency analysis         |
| `browserstack_test.py`      | Runs Selenium tests in 5 parallel threads on BrowserStack              |
| `downloaded_images/`        | Stores article images that were downloaded during scraping             |
| `requirements.txt`          | Contains required Python dependencies                                  |
| `README.md`                 | Project documentation (this file)                                     |

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/misbahkhanum/selenium-elpais.git
cd selenium-elpais
