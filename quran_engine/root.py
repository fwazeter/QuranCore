class Root:
    def __init__(self, id: int, text_arabic: str, meaning: str):
        self.__id = id
        self.__text_arabic = text_arabic
        self.__meaning = meaning

    def to_dict(self) -> dict:
        """Export Root as a dictionary."""
        return {
            'id': self.__id,
            'text_arabic': self.__text_arabic,
            'meaning': self.__meaning
        }
