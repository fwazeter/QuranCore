"""
Represents a root word in the Quran.

The Root class serves as a representation of Arabic roots, which are essential
for linguistic and thematic analysis. Each root has a corresponding meaning
that provides semantic context.

**Attributes:**
    text (str): The Arabic root text.
    meaning (str): The semantic meaning of the root in English or another language.
"""
class Root:
    """
    **Root** represents a root word in the Quran.

    **Attributes:**
        __text (str): The Arabic root text.
        __meaning (str): The meaning of the root in English or another language.
    """

    def __init__(self, text: str, meaning: str):
        """
        **Initialize a Root with the required attributes.**

        **Attributes:**
            text (str): The Arabic root text.
            meaning (str): The meaning of the root in English or another language.
        """
        self.__text = text if text is not None else ''
        self.__meaning = meaning if meaning is not None else ''

    @classmethod
    def from_dict(cls, data: dict) -> 'Root':
        """
        **Create a Root instance from a dictionary.**

        **Attributes:**
            data (dict): A dictionary containing the text and meaning of the root.

        **Returns:**
            Root: An instance of the Root class.
        """
        return cls(
            data.get('text', ''),
            data.get('meaning', '')
        )

    def to_dict(self) -> dict:
        """
        **Serialize the Root as a dictionary.**

        **Purpose:**
        Converts the Root instance into a dictionary format, suitable for storage,
        JSON export, or data transfer.

        **Returns:**
            dict: The dictionary representation of the Root.
        """
        return {
            'text': self.__text,
            'meaning': self.__meaning
        }

    def get_text(self) -> str:
        """
        **Get the Arabic root text.**

        **Returns:**
            str: The Arabic root text.
        """
        return self.__text

    def set_text(self, text: str) -> None:
        """
        **Set the Arabic root text.**

        **Purpose:**
        Updates the text of the root. If None is provided, it defaults to an empty string.

        **Attributes:**
            text (str): The new Arabic root text to be set.
        """
        self.__text = text if text is not None else ''

    def get_meaning(self) -> str:
        """
        **Get the meaning of the root.**

        **Returns:**
            str: The semantic meaning of the root.
        """
        return self.__meaning

    def set_meaning(self, meaning: str) -> None:
        """
        **Set the meaning of the root.**

        **Purpose:**
        Updates the meaning of the root. If None is provided, it defaults to an empty string.

        **Attributes:**
            meaning (str): The new meaning of the root to be set.
        """
        self.__meaning = meaning if meaning is not None else ''
