from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"


class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object) -> bool:

        if not isinstance(value, self.__class__):
            raise ValueError(f"value is not an instance of {self.__class__}")

        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"
