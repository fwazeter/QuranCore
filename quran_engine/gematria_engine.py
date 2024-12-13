"""
Utility class for calculating gematric values of Arabic text.

This class provides functionality to calculate the gematria of Arabic text
based on the traditional system. Custom gematria mappings can also be provided.

**Attributes:**
    DEFAULT_GEMATRIA_MAP (dict): Default mapping of Arabic characters to gematria values.
    __gematria_map (dict): The gematria map used for calculations. Can be user-defined or default.
"""
import re


class GematriaEngine:
    """
    **GematriaEngine** handles gematria calculations for Arabic characters.

    **Attributes:**
        DEFAULT_GEMATRIA_MAP (dict): Default mapping of Arabic characters to their gematria values.
        __gematria_map (dict): The gematria mapping being used in calculations.
    """

    DEFAULT_GEMATRIA_MAP = {
        'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
        'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
        'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900,
        'غ': 1000
    }

    def __init__(self, gematria_map: dict = None):
        """
        **Initialize the GematriaEngine.**

        **Purpose:**
        Initializes the gematria engine with a custom mapping or the default
        Arabic gematria system.

        **Attributes:**
            gematria_map (dict): A custom gematria map. Defaults to the standard Arabic gematria system.
        """
        self.__gematria_map = gematria_map if gematria_map else self.DEFAULT_GEMATRIA_MAP

    def calculate_gematria(self, text: str) -> int:
        """
        **Calculate the gematria of the given Arabic text.**

        **Purpose:**
        Returns the sum of the gematria values for each character in the input text.

        **Process:**
            1. Normalize input text (handle None, remove diacritics, strip non-Arabic characters).
            2. Sum up the gematria values for each character in the text.

        **Attributes:**
            text (str): The Arabic text to calculate gematria for.

        **Returns:**
            int: The total gematria value of the text.
        """
        if not text:
            return 0

        text = self._sanitize_text(text)
        return sum(self.__gematria_map.get(char, 0) for char in text)

    def get_gematria_map(self) -> dict:
        """
        **Get the gematria mapping being used.**

        **Purpose:**
        Retrieves the current gematria mapping being used.

        **Returns:**
            dict: The dictionary containing the gematria mapping.
        """
        return self.__gematria_map

    def set_gematria_map(self, gematria_map: dict) -> None:
        """
        **Set a custom gematria map.**

        **Purpose:**
        Replaces the default or existing gematria map with a user-specified map.

        **Attributes:**
            gematria_map (dict): The new gematria map to be used in calculations.
        """
        self.__gematria_map = gematria_map

    def _sanitize_text(self, text: str) -> str:
        """
        **Sanitize the Arabic text for gematria calculation.**

        **Purpose:**
        Removes non-Arabic characters and optional diacritics.

        **Process:**
            1. Remove diacritics (optional) from the Arabic text.
            2. Remove any non-Arabic characters, only allowing Arabic letters.

        **Attributes:**
            text (str): The input text to be sanitized.

        **Returns:**
            str: The sanitized text containing only Arabic characters.
        """
        if not text:
            return ''

        # Remove diacritics (if applicable) and non-Arabic characters
        text = re.sub(r'[^ء-ي]', '', text)  # Retain only Arabic characters
        return text
