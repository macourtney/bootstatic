from blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode, block_type_to_html_node
from textnode import TextNode, TextNodeType
import shutil
import os

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(block_type_to_html_node(block_type, block))
    return ParentNode("div", html_nodes)

def delete_public():
    print("Deleting public")
    if os.path.exists("public"):
        shutil.rmtree("public")

def copy_static_files():
    print("Copying static files")
    if os.path.exists("static"):
        shutil.copytree("static", "public")


def main():
    delete_public()
    copy_static_files()
    return """
    Scan content/
    Find all markdown files
    Convert each markdown file to an html file
    Create a public/ folder for all the html files
    """

if __name__ == "__main__":
    print(main())