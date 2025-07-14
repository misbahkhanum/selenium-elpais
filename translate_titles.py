from googletrans import Translator

# List of titles to translate
titles = [
    "Destructiva generación de incendios",
    # Add more titles here if needed
]

translator = Translator()
for idx, title in enumerate(titles, start=1):
    translated = translator.translate(title, src='es', dest='en')
    print(f"{idx}. Spanish: {title}")
    print(f"   English: {translated.text}\n")
