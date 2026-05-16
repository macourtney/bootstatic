import sys
import shutil
import os
from extract import extract_title
from blocks import markdown_to_blocks, block_to_block_type
from parentnode import ParentNode, block_type_to_html_node

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_nodes.append(block_type_to_html_node(block_type, block))
    return ParentNode("div", html_nodes)

def delete_docs():
    print("Deleting docs")
    if os.path.exists("docs"):
        shutil.rmtree("docs")

def copy_static_files():
    print("Copying static files")
    if os.path.exists("static"):
        shutil.copytree("static", "docs")

def generate_page(base_path, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace("href=\"", f"href=\"{base_path}")
    template = template.replace("src=\"", f"src=\"{base_path}")

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(base_path, dir_path_content, template_path, dest_dir_path):
    markdown_extensions = [".md"]
    
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        if os.path.isdir(from_path):
            generate_pages_recursive(base_path, from_path, template_path, os.path.join(dest_dir_path, filename))
        elif filename.endswith(tuple(markdown_extensions)):
            dest_path = os.path.join(dest_dir_path, filename[:-3] + ".html")
            generate_page(base_path, from_path, template_path, dest_path)

def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 main.py <base_path>")
    base_path = sys.argv[1]
    if len(base_path) == 0:
        base_path = "/"
    delete_docs()
    copy_static_files()

    generate_pages_recursive(base_path, "content", "template.html", "docs")
    return "Generating static files complete!"

if __name__ == "__main__":
    print(main())