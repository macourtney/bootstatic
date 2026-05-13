from textnode import TextNode, TextNodeType
from extract import find_all_markdown_images, find_all_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextNodeType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Unclosed delimiter found")

        for i, text in enumerate(parts):
            if text == "":
                continue
            elif i % 2 == 0:
                new_nodes.append(TextNode(text, TextNodeType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextNodeType.TEXT:
            new_nodes.append(node)
            continue
        matches = find_all_markdown_images(node.text)
        start_index = 0
        for match in matches:
            alt_text = match.group(1)
            url = match.group(2)
            if start_index != match.start():
                text_before = node.text[start_index:match.start()]
                new_nodes.append(TextNode(text_before, TextNodeType.TEXT))
            new_nodes.append(TextNode(alt_text, TextNodeType.IMAGE, url))
            start_index = match.end()
        if start_index < len(node.text):
            text_after = node.text[start_index:]
            new_nodes.append(TextNode(text_after, TextNodeType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.type != TextNodeType.TEXT:
            new_nodes.append(node)
            continue
        matches = find_all_markdown_links(node.text)
        start_index = 0
        for match in matches:
            alt_text = match.group(1)
            url = match.group(2)
            if start_index != match.start():
                text_before = node.text[start_index:match.start()]
                new_nodes.append(TextNode(text_before, TextNodeType.TEXT))
            new_nodes.append(TextNode(alt_text, TextNodeType.LINK, url))
            start_index = match.end()
        if start_index < len(node.text):
            text_after = node.text[start_index:]
            new_nodes.append(TextNode(text_after, TextNodeType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    if not text:
        return [TextNode("", TextNodeType.TEXT)]
    nodes = [TextNode(text, TextNodeType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextNodeType.BOLD)
    nodes = split_nodes_delimiter(nodes, "__", TextNodeType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextNodeType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextNodeType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextNodeType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
