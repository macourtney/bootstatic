from enum import Enum

class TextNodeType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, type: TextNodeType, url: str | None = None):
        self.text = text
        self.type = type
        self.url = url
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented
        return self.text == other.text and self.type == other.type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.type}, {self.url})"

