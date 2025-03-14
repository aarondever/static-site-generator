from enum import Enum

from .html_node import HTMLNode
from .leaf_node import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str = "") -> None:
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

    def to_html_node(self) -> HTMLNode:
        match self.text_type:
            case TextType.TEXT:
                return LeafNode(None, self.text)

            case TextType.BOLD:
                return LeafNode("b", self.text)

            case TextType.ITALIC:
                return LeafNode("i", self.text)

            case TextType.CODE:
                return LeafNode("code", self.text)

            case TextType.LINK:
                return LeafNode("a", self.text, {"href": self.url})

            case TextType.IMAGE:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})

        raise ValueError(f"Invalid text type: {self.text_type}")
