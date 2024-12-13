
"""
    Represents an Ayah (verse) in the Quran.
    Each Ayah contains multiple words and maintains its position in the Surah.
"""

class Ayah:
    def __init__(self, id: int, position: int, text_arabic: str, sanitized_text: str):
        self.__id = id
        self.__position = position
        self.__text_arabic = text_arabic
        self.__sanitized_text = sanitized_text
        self.__words = []

    def add_word(self, word: 'Word') -> None:
        """Add a Word to this Ayah."""
        self.__words.append(word)

    def word_count(self) -> int:
        """Count total words in this Ayah."""
        return len(self.__words)

    def gematric_sum(self) -> int:
        """Sum of gematric values of all words."""
        return sum(word.get_gematric_value() for word in self.__words)

    def to_dict(self) -> dict:
        """Export Ayah as a dictionary."""
        return {
            'id': self.__id,
            'position': self.__position,
            'text_arabic': self.__text_arabic,
            'words': [word.to_dict() for word in self.__words]
        }
