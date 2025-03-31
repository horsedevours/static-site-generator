from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    results = []
    for node in old_nodes:
        print(node)
        text = node.text
        if delimiter not in text:
            print(False)
            return
        else:
            print(True)
            i = 0
            print(text)
            print(text.split(delimiter))
            print(text.find(delimiter))
            print(text.find(delimiter, 21))
            print(text.find(delimiter, 32))