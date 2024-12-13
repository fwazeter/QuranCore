"""
    Represents an Ayah (verse) in the Quran.

    An Ayah contains multiple words and maintains its position in the Surah.

    Attributes:
    id (int): The unique identifier for the Ayah.
    position (int): The position of the Ayah within the Surah.
    text_arabic (str): The Arabic text of the Ayah.
    sanitized_text (str): The sanitized version of the Arabic text with diacritics removed.
    translation (str): The translation of the Ayah.
"""
class Ayah:

    def __init__(self, id: int, position: int, text_arabic: str, sanitized_text: str, translation: str):
        """
            **Initialize an Ayah with the required attributes.**

            **Attributes:**
                id (int): Unique identifier for the Ayah.
                position (int): Position of the Ayah in the Surah.
                text_arabic (str): The Arabic text of the Ayah.
                sanitized_text (str): Sanitized version of the text.
                translation (str): The translation of the Ayah.
        """
        self.__id = id
        self.__position = position
        self.__text_arabic = text_arabic if text_arabic is not None else ''  # Ensure no None values
        self.__sanitized_text = sanitized_text if sanitized_text is not None else ''  # Ensure no None values
        self.__translation = translation if isinstance(translation, str) else ''

    @classmethod
    def from_dict(cls, data: dict) -> 'Ayah':
        """
            **Create an Ayah instance from a dictionary.**

            **Attributes:**
                data (dict): Dictionary containing Ayah data.

            **Returns:**
                Ayah: An instance of the Ayah class.
        """
        return cls(
            data.get('id', 0),
            data.get('position', 0),
            data.get('text_arabic', ''),
            data.get('sanitized_text', ''),
            data.get('translation', '')
        )

    def to_dict(self) -> dict:
        """
            **Serialize the Ayah as a dictionary.**

            **Returns:**
                dict: The dictionary representation of the Ayah.
        """
        return {
            'id': self.__id,
            'position': self.__position,
            'text_arabic': self.__text_arabic,
            'sanitized_text': self.__sanitized_text,
            'translation': self.__translation
        }

    def get_id(self) -> int:
        """
        **Get the ID of the Ayah.**

        **Returns:**
            int: The unique identifier of the Ayah.
        """
        return self.__id

    def set_id(self, id: int) -> None:
        """
        **Set the ID of the Ayah.**

        **Attributes:**
            id (int): The new ID to set for the Ayah.
        """
        self.__id = id

    def get_position(self) -> int:
        """
        **Get the position of the Ayah.**

        **Returns:**
            int: The position of the Ayah within the Surah.
        """
        return self.__position

    def set_position(self, position: int) -> None:
        """
        **Set the position of the Ayah.**

        **Attributes:**
            position (int): The new position of the Ayah in the Surah.
        """
        self.__position = position

    def get_text_arabic(self) -> str:
        """
        **Get the Arabic text of the Ayah.**

        **Returns:**
            str: The Arabic text of the Ayah.
        """
        return self.__text_arabic

    def set_text_arabic(self, text: str) -> None:
        """
        **Set the Arabic text of the Ayah.**

        **Attributes:**
            text (str): The Arabic text to set for the Ayah.
        """
        self.__text_arabic = text if text is not None else ''  # Convert None to an empty string

    def get_sanitized_text(self) -> str:
        """
        **Get the sanitized text of the Ayah.**

        **Returns:**
            str: The sanitized Arabic text of the Ayah.
        """
        return self.__sanitized_text

    def set_sanitized_text(self, text: str) -> None:
        """
        **Set the sanitized text of the Ayah.**

        **Attributes:**
            text (str): The sanitized version of the Arabic text to be set.
        """
        if isinstance(text, str):
            self.__sanitized_text = text

    def get_translation(self) -> str:
        """
        **Get the translation of the Ayah.**

        **Returns:**
            str: The translation of the Ayah.
        """
        return self.__translation

    def set_translation(self, translation: str) -> None:
        """
        **Set the translation of the Ayah.**

        **Attributes:**
            translation (str): The translation to set for the Ayah.
        """
        if isinstance(translation, str):
            self.__translation = translation

    def word_count(self) -> int:
        """
        **Return the number of words in the Arabic text.**

        **Process:**
        1. Split the Arabic text into words using whitespace as the delimiter.
        2. Return the total number of words.

        **Returns:**
            int: The number of words in the Arabic text.
        """
        if self.__text_arabic:
            return len(self.__text_arabic.split())
        if not self.__text_arabic:  # Handle None and empty strings
            return 0
