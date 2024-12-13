from quran_engine.gematria_engine import GematriaEngine
"""
    Represents a Word in an Ayah.
    Each Word has an associated gematric value and is linked to a Root.
"""

class Word:
    def __init__(self, id: int, text_arabic: str, root: 'Root', grammar: str):
        self.__id = id
        self.__text_arabic = text_arabic
        self.__root = root
        self.__grammar = grammar
        self.__gematric_value = self.__calculate_gematric_value()

    def __calculate_gematric_value(self) -> int:
        """Private method to calculate gematric value."""
        return sum(GematriaEngine.get_gematric_value(char) for char in self.__text_arabic)

    def get_gematric_value(self) -> int:
        """Return gematric value of the word."""
        return self.__gematric_value

    def to_dict(self) -> dict:
        """Export Word as a dictionary."""
        return {
            'id': self.__id,
            'text_arabic': self.__text_arabic,
            'gematric_value': self.__gematric_value,
            'root': self.__root.to_dict() if self.__root else None
        }
