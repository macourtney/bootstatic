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
