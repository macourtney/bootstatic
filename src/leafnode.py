from textnode import TextNode, TextNodeType
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = None
        self.props = props
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"LeafNode('{self.tag}', '{self.value}', {self.props})"
    
    def to_html(self):
        if self.value is None:
            raise ValueError(f"LeafNode must have a value. Node: {self}")
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self._props_to_html()}>{self.value}</{self.tag}>"
    
    def _props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html

def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    if text_node.type == TextNodeType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.type == TextNodeType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.type == TextNodeType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.type == TextNodeType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.type == TextNodeType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.type == TextNodeType.IMAGE:
        return LeafNode("img", text_node.text, {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text node type: {text_node.type}")