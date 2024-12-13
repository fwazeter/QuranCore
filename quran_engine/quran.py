
"""
    The Quran class acts as the main entry point to the Quranic data system.
    It aggregates all Surahs, provides utilities to query Surahs, and
    calculates totals like total word count and total gematric sum.
"""

class Quran:
    def __init__(self):
        self.__surahs = []  # Private list of Surah objects

    def add_surah(self, surah: 'Surah') -> None:
        """Add a Surah to the Quran."""
        self.__surahs.append(surah)

    def get_surah(self, surah_id: int) -> 'Surah':
        """Return a specific Surah by its ID."""
        return next((s for s in self.__surahs if s.id == surah_id), None)

    def total_word_count(self) -> int:
        """Count total words in the entire Quran."""
        return sum(surah.total_word_count() for surah in self.__surahs)

    def total_gematric_sum(self) -> int:
        """Return total gematria of all words in the Quran."""
        return sum(surah.total_gematric_sum() for surah in self.__surahs)

    def export_to_json(self) -> dict:
        """Export Quran to JSON-compatible dictionary."""
        return {'surahs': [surah.to_dict() for surah in self.__surahs]}
