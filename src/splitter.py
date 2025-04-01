from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links

def split_nodes_bold(old_nodes):
    return split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

def split_nodes_code(old_nodes):
    return split_nodes_delimiter(old_nodes, "`", TextType.CODE)

def split_nodes_italic(old_nodes):
    return split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if text_type == TextType.TEXT or node.text_type != TextType.TEXT:
            results.append(node)
        else:
            text = node.text
            if text.count(delimiter) % 2 != 0:
                raise Exception("delimiters must be in matching pairs")
            st = split_text(text, delimiter, text_type)
            results.extend(st)
    return results


def split_text(text, delimiter, text_type):
    s = 0
    len_d = len(delimiter)
    fmted_text = False
    results = []
    while s < len(text):
        i = text.find(delimiter, s)
        if i == 0:
            j = text.find(delimiter, s + len_d)
            results.append(TextNode(text[s+len_d:j], text_type))
            s = j + len_d
        elif i != -1 and not fmted_text:
            results.append(TextNode(text[s:i], TextType.TEXT))
            fmted_text = True
            s = i + 1
        elif i != -1 and fmted_text:
            results.append(TextNode(text[s+len_d-1:i], text_type))
            fmted_text = False
            s = i + len_d
        else:
            results.append(TextNode(text[s:], TextType.TEXT))
            s = len(text)
    return results

def split_nodes_image(old_nodes):
    results = []
    for node in old_nodes:
        txt = node.text
        images = extract_markdown_images(txt)
        if not images:
            results.append(node)
            continue
        start = 0
        for image in images:
            i = txt.find(f"![{image[0]}]")
            if i == 0:
                results.append(TextNode(image[0], TextType.IMAGE, image[1]))
            else:
                results.append(TextNode(txt[start:i], TextType.TEXT))
                results.append(TextNode(image[0], TextType.IMAGE, image[1]))
            start = i + len(image[0]) + len(image[1]) + 5
        if start < len(txt):
            results.append(TextNode(txt[start:], TextType.TEXT))
    return results


def split_nodes_link(old_nodes):
    results = []
    for node in old_nodes:
        txt = node.text
        links = extract_markdown_links(txt)
        if not links:
            results.append(node)
            continue
        start = 0
        for link in links:
            i = txt.find(f"[{link[0]}]")
            if i == 0:
                results.append(TextNode(link[0], TextType.LINK, link[1]))
            else:
                results.append(TextNode(txt[start:i], TextType.TEXT))
                results.append(TextNode(link[0], TextType.LINK, link[1]))
            start = i + len(link[0]) + len(link[1]) + 4
        if start < len(txt):
            results.append(TextNode(txt[start:], TextType.TEXT))
    return results