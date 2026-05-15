from blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode, block_type_to_html_node
from textnode import TextNode, TextNodeType


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(block_type_to_html_node(block_type, block))
    return ParentNode("div", html_nodes)


def main():
    tnode1 = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
    return tnode1

if __name__ == "__main__":
    print(main())