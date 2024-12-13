"""
Represents a Surah (chapter) in the Quran.

A Surah contains multiple Ayahs and maintains metadata such as name, classification, and revelation order.
It supports operations for adding Ayahs, calculating total word counts, and gematric sums.

**Attributes:**
    id (int): The unique identifier for the Surah.
    name (str): The name of the Surah.
    revelation_order (int): The order in which the Surah was revealed.
    total_ayahs (int): The total number of Ayahs in the Surah.
    classification (str): The classification of the Surah (Meccan or Medinan).
    ayah_class (type): The Ayah class type used to construct Ayah instances.
    ayahs (list): A list of Ayah objects contained in the Surah.
"""
from typing import List

class Surah:
    """Represents a Surah (chapter) in the Quran."""

    def __init__(self, id: int, name: str, revelation_order: int, total_ayahs: int, classification: str, ayah_class: type):
        """
        **Initialize a Surah with the required attributes.**

        **Attributes:**
            id (int): Unique identifier for the Surah.
            name (str): Name of the Surah.
            revelation_order (int): Order in which the Surah was revealed.
            total_ayahs (int): Total number of Ayahs in the Surah.
            classification (str): Classification of the Surah (Meccan or Medinan).
            ayah_class (type): The Ayah class type used to construct Ayah instances.
        """
        self.__id = id
        self.__name = name
        self.__revelation_order = revelation_order
        self.__total_ayahs = total_ayahs
        self.__classification = classification
        self.__ayah_class = ayah_class
        self.__ayahs: List = []

    @classmethod
    def from_xml(cls, surah_element, ayah_class: type) -> 'Surah':
        """
        **Create a Surah object from an XML element.**

        **Attributes:**
            surah_element (XML element): The XML element containing Surah data.
            ayah_class (type): The Ayah class type used to construct Ayah instances.

        **Returns:**
            Surah: An instance of the Surah class.
        """
        id = int(surah_element.get('index', 0))
        name = surah_element.get('name', 'Unknown')
        total_ayahs = len(surah_element.findall('aya'))
        revelation_order = int(surah_element.get('revelationOrder', 0))
        classification = 'Meccan'
        surah = cls(id, name, revelation_order, total_ayahs, classification, ayah_class)

        for aya_element in surah_element.findall('aya'):
            ayah_index = int(aya_element.get('index', 0))
            ayah_text = aya_element.get('text', '')
            ayah = ayah_class(ayah_index, ayah_index, ayah_text, '')
            surah.add_ayah(ayah)

        return surah

    @classmethod
    def from_dict(cls, data: dict, ayah_class: type) -> 'Surah':
        """
        **Create a Surah object from a dictionary.**

        **Attributes:**
            data (dict): Dictionary containing Surah data.
            ayah_class (type): The Ayah class type used to construct Ayah instances.

        **Returns:**
            Surah: An instance of the Surah class.
        """
        surah = cls(
            data.get('id', 0),
            data.get('name', 'Unknown'),
            data.get('revelation_order', 0),
            data.get('total_ayahs', 0),
            data.get('classification', 'Unknown'),
            ayah_class
        )
        for ayah_data in data.get('ayahs', []):
            ayah = ayah_class.from_dict(ayah_data)
            surah.add_ayah(ayah)

        return surah

    def add_ayah(self, ayah) -> None:
        """
        **Add an Ayah to this Surah.**

        **Attributes:**
            ayah (Ayah): The Ayah object to be added to the Surah.
        """
        self.__ayahs.append(ayah)

    def total_word_count(self) -> int:
        """
        **Count total words in this Surah.**

        **Returns:**
            int: Total number of words in all Ayahs of the Surah.
        """
        return sum(ayah.word_count() for ayah in self.__ayahs)

    def total_gematric_sum(self) -> int:
        """
        **Calculate the total gematria for all words in the Surah.**

        **Returns:**
            int: Total gematria value of all words in the Surah.
        """
        return sum(ayah.gematric_sum() for ayah in self.__ayahs)

    def to_dict(self) -> dict:
        """
        **Export Surah as a dictionary.**

        **Returns:**
            dict: The dictionary representation of the Surah.
        """
        return {
            'id': self.__id,
            'name': self.__name,
            'revelation_order': self.__revelation_order,
            'total_ayahs': self.__total_ayahs,
            'classification': self.__classification,
            'ayahs': [ayah.to_dict() for ayah in self.__ayahs]
        }

    def get_id(self) -> int:
        """Get the ID of the Surah."""
        return self.__id

    def get_name(self) -> str:
        """Get the name of the Surah."""
        return self.__name

    def get_revelation_order(self) -> int:
        """Get the revelation order of the Surah."""
        return self.__revelation_order

    def get_total_ayahs(self) -> int:
        """Get the total number of Ayahs in the Surah."""
        return self.__total_ayahs

    def get_classification(self) -> str:
        """Get the classification of the Surah (Meccan or Medinan)."""
        return self.__classification

    def get_ayahs(self) -> List:
        """Get the list of Ayahs in the Surah."""
        return self.__ayahs

    def set_id(self, id: int) -> None:
        """Set the ID of the Surah."""
        self.__id = id

    def set_name(self, name: str) -> None:
        """Set the name of the Surah."""
        self.__name = name

    def set_revelation_order(self, revelation_order: int) -> None:
        """Set the revelation order of the Surah."""
        self.__revelation_order = revelation_order

    def set_total_ayahs(self, total_ayahs: int) -> None:
        """Set the total number of Ayahs in the Surah."""
        self.__total_ayahs = total_ayahs

    def set_classification(self, classification: str) -> None:
        """Set the classification of the Surah (Meccan or Medinan)."""
        self.__classification = classification

    def set_ayahs(self, ayahs: List) -> None:
        """Set the list of Ayahs in the Surah."""
        self.__ayahs = ayahs
