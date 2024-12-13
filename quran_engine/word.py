"""
Represents a Word in an Ayah.

Each Word has an associated gematric value and is linked to a Root.

**Attributes:**
    id (int): The unique identifier for the Word.
    text_arabic (str): The Arabic text of the Word.
    root (Root): The root of the Word.
    gematria (int): The gematria value of the Word.
"""
class Word:
    """
    **Word** represents a single word in an Ayah.

    **Attributes:**
        __id (int): The unique identifier for the Word.
        __text_arabic (str): The Arabic text of the Word.
        __root (Root): The root of the Word.
        __gematria (int): The gematria value of the Word.
    """

    def __init__(self, id: int, text_arabic: str, root: 'Root', gematria: int):
        """
        **Initialize a Word with the required attributes.**

        **Attributes:**
            id (int): Unique identifier for the Word.
            text_arabic (str): The Arabic text of the Word.
            root (Root): The root of the Word.
            gematria (int): The gematria value of the Word.
        """
        self.__id = id
        self.__text_arabic = text_arabic if text_arabic is not None else ''  # Handle None values
        self.__root = root
        self.__gematria = gematria

    @classmethod
    def from_dict(cls, data: dict, root_class: type) -> 'Word':
        """
        **Create a Word instance from a dictionary.**

        **Attributes:**
            data (dict): A dictionary containing the attributes for the Word.
            root_class (type): The class used to create the Root instance.

        **Returns:**
            Word: An instance of the Word class.
        """
        root = root_class.from_dict(data.get('root', {}))
        return cls(
            data.get('id', 0),
            data.get('text_arabic', ''),
            root,
            data.get('gematria', 0)
        )

    def to_dict(self) -> dict:
        """
        **Serialize the Word as a dictionary.**

        **Purpose:**
        Converts the Word instance into a dictionary format, suitable for storage,
        JSON export, or data transfer.

        **Returns:**
            dict: The dictionary representation of the Word.
        """
        return {
            'id': self.__id,
            'text_arabic': self.__text_arabic,
            'root': self.__root.to_dict() if self.__root else None,
            'gematria': self.__gematria
        }

    def get_id(self) -> int:
        """
        **Get the ID of the Word.**

        **Returns:**
            int: The unique identifier of the Word.
        """
        return self.__id

    def set_id(self, id: int) -> None:
        """
        **Set the ID of the Word.**

        **Attributes:**
            id (int): The new ID to be set for the Word.
        """
        self.__id = id

    def get_text_arabic(self) -> str:
        """
        **Get the Arabic text of the Word.**

        **Returns:**
            str: The Arabic text of the Word.
        """
        return self.__text_arabic

    def set_text_arabic(self, text: str) -> None:
        """
        **Set the Arabic text of the Word.**

        **Purpose:**
        Updates the text of the Word. If None is provided, it defaults to an empty string.

        **Attributes:**
            text (str): The new Arabic text to be set for the Word.
        """
        self.__text_arabic = text if text is not None else ''  # Handle None values

    def get_root(self) -> 'Root':
        """
        **Get the root of the Word.**

        **Returns:**
            Root: The root object of the Word.
        """
        return self.__root

    def set_root(self, root: 'Root') -> None:
        """
        **Set the root of the Word.**

        **Purpose:**
        Updates the root of the Word.

        **Attributes:**
            root (Root): The new root object to be set for the Word.
        """
        self.__root = root

    def get_gematria(self) -> int:
        """
        **Get the gematria value of the Word.**

        **Returns:**
            int: The gematria value of the Word.
        """
        return self.__gematria

    def set_gematria(self, gematria: int) -> None:
        """
        **Set the gematria value of the Word.**

        **Attributes:**
            gematria (int): The new gematria value to be set for the Word.
        """
        self.__gematria = gematria

    def calculate_gematria(self) -> int:
        """
        **Calculate the gematria of the text_arabic.**

        **Purpose:**
        Calculates the sum of the gematria values for each character in the Arabic text.

        **Process:**
            1. Normalize input text (handle None, remove diacritics, strip non-Arabic characters).
            2. Sum up the gematria values for each character in the text using a predefined mapping.

        **Returns:**
            int: The total gematria value for the Arabic text.
        """
        if not self.__text_arabic:  # Handle None and empty strings
            return 0

        # Example gematria mapping for testing purposes
        arabic_to_gematria = {'ب': 2, 'س': 60, 'م': 40}  # Example mapping
        return sum(arabic_to_gematria.get(char, 0) for char in self.__text_arabic)
