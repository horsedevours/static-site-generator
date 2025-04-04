import os, shutil
import htmler
from textnode import TextNode, TextType

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("# ").rstrip()

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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    ls = os.listdir(dir_path_content)

    for l in ls:
        src_path = os.path.join(dir_path_content, l)
        dest_path = os.path.join(dest_dir_path, l).removesuffix(".md")
        if os.path.isfile(src_path) and l.endswith(".md"):
            generate_page(src_path, template_path, dest_path + ".html")
        elif os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path) as f:
        md = f.read()
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
    generate_pages_recursive("content", "template.html", "public")

main()