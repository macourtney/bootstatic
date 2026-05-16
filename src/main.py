import genericpath
from extract import extract_title
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

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    print("HTML NODE: ", html_node)
    html_content = html_node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    markdown_extensions = [".md"]
    
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isdir(from_path):
            generate_pages_recursive(from_path, template_path, os.path.join(dest_dir_path, filename))
        elif filename.endswith(tuple(markdown_extensions)):
            dest_path = os.path.join(dest_dir_path, filename[:-3] + ".html")
            generate_page(from_path, template_path, dest_path)

def main():
    delete_public()
    copy_static_files()

    generate_pages_recursive("content", "template.html", "public")
    return "Generating static files complete!"

if __name__ == "__main__":
    print(main())