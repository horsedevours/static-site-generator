import os, shutil
import htmler
from textnode import TextNode, TextType


print("hello world")

def copy_dir_contents(src="static", dest="public"):
    if os.path.exists(dest):
        shutil.rmtree(dest)  
    os.mkdir(dest)
    ls = os.listdir(src)
    for l in ls:
        src_path = os.path.join(src, l)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest)
        elif os.path.isdir(src_path):
            dest_path = os.path.join(dest, l)
            copy_dir_contents(src_path, dest_path)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").rstrip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path) as f:
        md = f.read()
    print(md)
    html = htmler.markdown_to_html_node(md).to_html()
    title = extract_title(md)

    with open(template_path) as t:
        templ = t.read()
    templ = templ.replace("{{ Title }}", title)
    templ = templ.replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    d = open(dest_path, "w")
    d.write(templ)
    d.close

def main():
    copy_dir_contents()
    generate_page("content/index.md", "template.html", "public/index.html")

main()