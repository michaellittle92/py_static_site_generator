from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.TextType = text_type
        self.url = url

    def __eq__(self, value):
        if self == value:
            return True
        return False
    def __repr__(self):
        return f"TextNode({self.text}, {self.TextType, self.url})"