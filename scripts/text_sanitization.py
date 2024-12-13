import re

def sanitize_arabic_text(text):
    """
    Sanitizes Arabic text by removing diacritics and normalizing Arabic characters.
    """
    print(f"Sanitizing text: {text}")
    text = re.sub(r'[ًٌٍَُِّْ]', '', text)  # Remove diacritics
    text = text.replace('أ', 'ا').replace('إ', 'ا').replace('آ', 'ا')  # Normalize alif
    text = text.replace('ى', 'ي')  # Normalize ya
    text = text.replace('ة', 'ه')  # Normalize ta marbuta
    print(f"Sanitized text: {text}")
    return text