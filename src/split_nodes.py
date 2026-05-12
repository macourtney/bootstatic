from textnode import TextNode, TextNodeType

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
