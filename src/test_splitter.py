import unittest

from splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitter(unittest.TestCase):

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(
            [TextNode("This is text with a " , TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)],
            new_nodes
        )

    def test_starts_bold(self):
        node = TextNode("**Bold** this is", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(
            [TextNode("Bold" , TextType.BOLD), TextNode(" this is", TextType.TEXT)],
            new_nodes
        )
    
    def test_multiple_italics(self):
        node = TextNode("This has some _italic text_", TextType.TEXT)
        node2 = TextNode("And some _more italic_ text", TextType.TEXT)
        node3 = TextNode("_Italic text_ is everywhere, or hadn't you _heard?_", TextType.TEXT)
        node4 = TextNode("_How about some_ _back to back_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2, node3, node4], "_", TextType.ITALIC)

        self.assertEqual(
            [TextNode("This has some ", TextType.TEXT), TextNode("italic text", TextType.ITALIC),
             TextNode("And some ", TextType.TEXT), TextNode("more italic", TextType.ITALIC), TextNode(" text", TextType.TEXT),
             TextNode("Italic text", TextType.ITALIC), TextNode(" is everywhere, or hadn't you ", TextType.TEXT), TextNode("heard?", TextType.ITALIC),
             TextNode("How about some", TextType.ITALIC), TextNode(" ", TextType.TEXT), TextNode("back to back", TextType.ITALIC)],
             new_nodes
        )
    
    def test_text(self):
        node = TextNode("Nothing to see here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], None, TextType.TEXT)

        self.assertEqual([TextNode("Nothing to see here", TextType.TEXT)], new_nodes)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) with some more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" with some more text", TextType.TEXT)
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.groogle.com) and another [second link](https://github.wakka-wakka.com/wiggity-woowoo) with some more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        print(new_nodes)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.groogle.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://github.wakka-wakka.com/wiggity-woowoo"
                ),
                TextNode(" with some more text", TextType.TEXT)
            ],
            new_nodes,
        )