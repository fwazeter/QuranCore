
"""
    Represents a Surah (chapter) in the Quran.
    Each Surah contains multiple Ayahs and metadata like name, classification,
    and revelation order.
"""

class Surah:
    def __init__(self, id: int, name: str, revelation_order: int, total_ayahs: int, classification: str):
        self.__id = id
        self.__name = name
        self.__revelation_order = revelation_order
        self.__total_ayahs = total_ayahs
        self.__classification = classification  # Meccan or Medinan
        self.__ayahs = []

    def add_ayah(self, ayah: 'Ayah') -> None:
        """Add an Ayah to this Surah."""
        self.__ayahs.append(ayah)

    def total_word_count(self) -> int:
        """Count total words in this Surah."""
        return sum(ayah.word_count() for ayah in self.__ayahs)

    def total_gematric_sum(self) -> int:
        """Calculate the total gematria for all words in the Surah."""
        return sum(ayah.gematric_sum() for ayah in self.__ayahs)

    def to_dict(self) -> dict:
        """Export Surah as a dictionary."""
        return {
            'id': self.__id,
            'name': self.__name,
            'revelation_order': self.__revelation_order,
            'total_ayahs': self.__total_ayahs,
            'classification': self.__classification,
            'ayahs': [ayah.to_dict() for ayah in self.__ayahs]
        }
