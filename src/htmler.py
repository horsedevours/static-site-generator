import blocker
from block import BlockType, block_to_block_type
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes
from htmlnode import LeafNode, ParentNode

def markdown_to_html_node(markdown):
    blocks = list(filter(None, blocker.markdown_to_blocks(markdown)))
    elements = []
    for block in blocks:
        type = block_to_block_type(block)
        match (type):
            case BlockType.CODE:
                code = text_node_to_html_node(TextNode("".join(list(map(str.lstrip, block.strip('`').splitlines(True)))), TextType.CODE))
                pre = ParentNode("pre", [code])
                elements.append(pre)
            case BlockType.PARAGRAPH:
                minus_new_lines = " ".join(list(map(str.lstrip, block.splitlines()))) 
                text_nodes = text_to_textnodes(minus_new_lines)
                contents = []
                for node in text_nodes:
                    contents.append(text_node_to_html_node(node))
                elements.append(ParentNode("p", contents))
            case BlockType.HEADING:
                stripped = block.strip("# \n")
                text_nodes = text_to_textnodes(stripped)
                contents = []
                for node in text_nodes:
                    contents.append(text_node_to_html_node(node))
                elements.append(ParentNode("h" + str(block.count("#")), contents))
            case BlockType.O_LIST:
                lines = list(map(str.strip, block.split("\n")))
                for i in range(len(lines)):
                    lines[i] = lines[i].removeprefix(f"{i+1}. ").strip()
                lis = []
                for line in lines:
                    text_nodes = text_to_textnodes(line)
                    contents = []
                    for node in text_nodes:
                        contents.append(text_node_to_html_node(node))
                    lis.append(ParentNode("li", contents))
                elements.append(ParentNode("ol", lis))
            case BlockType.U_LIST:
                lines = list(map(lambda l: l.lstrip("- "), block.splitlines()))
                lis = []
                for line in lines:
                    text_nodes = text_to_textnodes(line)
                    contents = []
                    for node in text_nodes:
                        contents.append(text_node_to_html_node(node))
                    lis.append(ParentNode("li", contents))
                elements.append(ParentNode("ul", lis))
            case BlockType.QUOTE:
                text = "".join(list(map(lambda l: l.removeprefix(">").lstrip(), block.splitlines(True))))
                text_nodes = text_to_textnodes(text)
                contents = []
                for node in text_nodes:
                    contents.append(text_node_to_html_node(node))
                elements.append(ParentNode("blockquote", contents))
            case _:
                text_nodes = text_to_textnodes(block)
    return ParentNode("div", elements)