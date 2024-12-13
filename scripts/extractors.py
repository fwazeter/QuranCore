from scripts.text_sanitization import sanitize_arabic_text

def extract_words(ayah_text):
    """
    Extracts words from an Ayah and calculates their gematric values.
    """
    words = ayah_text.split()
    sanitized_words = [sanitize_arabic_text(word) for word in words]
    gematric_values = [calculate_gematric_value(word) for word in sanitized_words]
    return sanitized_words, gematric_values



"""Handles root extraction from words (basic logic for now)"""
def extract_roots(words):
    roots = []
    for word in words:
        root = word[:3] if len(word) > 3 else word
        roots.append(root)
    return roots

# Global gematria mapping for Arabic characters
GEMATRIA_MAPPING = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7,
    'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40,
    'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
    'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

def calculate_gematric_value(word):
    """
    Calculates the gematric value of an Arabic word using GEMATRIA_MAPPING.
    """
    return sum(GEMATRIA_MAPPING.get(char, 0) for char in word)

