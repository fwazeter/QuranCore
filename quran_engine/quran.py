"""
Represents the Quran as a collection of Surahs (chapters).

The Quran class serves as the main entry point to the Quranic data system.
It aggregates all Surahs, provides utilities to query Surahs, and calculates
totals like total word count and total gematric sum.

**Attributes:**
    surahs (list): A list of Surah objects contained in the Quran.
    surah_class (type): The Surah class type used to construct Surah instances.
"""
from typing import List


class Quran:
    """
    **Quran** represents the entire Quran and provides access to its Surahs.

    **Attributes:**
        __surahs (list): A list of Surah objects contained in the Quran.
        __surah_class (type): The Surah class type used to construct Surah instances.
    """
    def __init__(self, surah_class: type):
        """
        **Initialize the Quran with a Surah class reference.**

        **Attributes:**
            surah_class (type): The Surah class type used to construct Surah instances.
        """
        self.__surahs: List = []
        self.__surah_class = surah_class

    @classmethod
    def from_dict(cls, data: dict, surah_class: type) -> 'Quran':
        """
        **Create a Quran object from a dictionary.**

        **Attributes:**
            data (dict): Dictionary containing Quran data.
            surah_class (type): The Surah class type used to construct Surah instances.

        **Process:**
            1. Extract Surah data from the dictionary.
            2. Create a Surah instance for each Surah in the data.
            3. Add each Surah to the Quran instance.

        **Returns:**
            Quran: An instance of the Quran class.
        """
        quran = cls(surah_class)
        for surah_data in data.get('surahs', []):
            surah = surah_class.from_dict(surah_data)
            quran.add_surah(surah)
        return quran

    def to_dict(self) -> dict:
        """
        **Export the Quran as a dictionary.**

        **Purpose:**
        Serializes the Quran's Surahs into a dictionary format for storage or data transfer.

        **Returns:**
            dict: The dictionary representation of the Quran.
        """
        return {
            'surahs': [surah.to_dict() for surah in self.__surahs]
        }

    def add_surah(self, surah) -> None:
        """
        **Add a Surah to the Quran.**

        **Purpose:**
        Adds a new Surah to the Quran's list of Surahs.

        **Attributes:**
            surah (Surah): The Surah object to be added to the Quran.
        """
        self.__surahs.append(surah)

    def get_surahs(self) -> List:
        """
        **Get the list of Surahs in the Quran.**

        **Returns:**
            list: A list of Surah objects contained in the Quran.
        """
        return self.__surahs

    def set_surahs(self, surahs: List) -> None:
        """
        **Set the list of Surahs in the Quran.**

        **Purpose:**
        Replaces the current list of Surahs with a new list.

        **Attributes:**
            surahs (list): The list of Surah objects to be set in the Quran.
        """
        self.__surahs = surahs
