import re

def extract_markdown_images(text):
    return re.findall(r"!\[([\w\s]+)\]\(([.\S]+)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[([\w\s]+)\]\(([.\S]+)\)", text)