from textnode import TextNode, TextNodeType
from htmlnode import HTMLNode
from leafnode import LeafNode


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
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Invalid text node type: {text_node.type}")


def main():
    tnode1 = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
    return tnode1

if __name__ == "__main__":
    print(main())