import re

image_regex = r"!\[(.*?)\]\((.*?)\)"
link_regex = r"\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text):
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    return re.findall(link_regex, text)

def find_all_markdown_images(text):
    return re.finditer(image_regex, text)

def find_all_markdown_links(text):
    return re.finditer(link_regex, text)

def extract_title(markdown):
    title_regex = r"(^|\n)# (.*?)(\n|$)"
    title = re.search(title_regex, markdown, flags=re.MULTILINE)
    if title:
        return title.group(2)
    else:
        raise ValueError("No title found in markdown file.")
