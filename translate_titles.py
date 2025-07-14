from googletrans import Translator
from collections import Counter
import re

# ✏️ Replace these with the 5 Spanish titles you scraped:
spanish_titles = [
    "La democracia en peligro",
    "El futuro de la economía española",
    "Una mirada crítica al sistema educativo",
    "El papel de la tecnología en la sociedad",
    "Reflexiones sobre la justicia social"
]

translator = Translator()
translated_titles = []

print("🔄 Translating titles...\n")

for title in spanish_titles:
    translation = translator.translate(title, src='es', dest='en')
    english_title = translation.text
    translated_titles.append(english_title)
    print(f"ES ➜ {title}")
    print(f"EN ➜ {english_title}\n")

# ── Word‑frequency analysis ───────────────────────────────
all_words = []
for title in translated_titles:
    # Lower‑case, keep only alphabetic words
    words = re.findall(r'\b[a-z]+\b', title.lower())
    all_words.extend(words)

counter = Counter(all_words)

print("\n🔍 Words repeated more than twice:")
for word, cnt in counter.items():
    if cnt > 2:
        print(f"{word}: {cnt}")
