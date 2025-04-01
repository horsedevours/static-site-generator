from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        if text_type == TextType.TEXT:
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
            results.append(TextNode(text[s:i], text_type))
            fmted_text = False
            s = i + len_d
        else:
            results.append(TextNode(text[s:], TextType.TEXT))
            s = len(text)
    return results