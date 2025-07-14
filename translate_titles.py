# translate_titles.py  – googletrans version  (no API key required)

from collections import Counter
import re
from googletrans import Translator
from scrape_articles import scrape_articles   # <-- re‑use your scraper

def translate_titles_es_to_en(titles):
    translator = Translator()
    return [translator.translate(t, src="es", dest="en").text for t in titles]

def main():
    # 1.  Get the first 5 article titles from your scraper
    articles = scrape_articles()
    spanish_titles = [a["title"] for a in articles]

    # 2.  Translate titles
    english_titles = translate_titles_es_to_en(spanish_titles)

    print("\n✅  Translated Titles")
    for es, en in zip(spanish_titles, english_titles):
        print(f"ES ➜ {es}\nEN ➜ {en}\n")

    # 3.  Word‑frequency analysis
    words = re.findall(r"\b\w+\b", " ".join(english_titles).lower())
    freq = Counter(words)
    print("🔍  Words repeated more than twice:")
    for w, c in freq.items():
        if c > 2:
            print(f"{w}: {c}")

if __name__ == "__main__":
    main()
