import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)

        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("One node", TextType.TEXT)
        node2 = TextNode("Another node", TextType.TEXT)

        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.CODE)

        self.assertNotEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("Same", TextType.TEXT, "www.abc.com")
        node2 = TextNode("Same", TextType.TEXT, "www.abd.com")

        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_link(self):
        node = TextNode("Linkypooh", TextType.LINK, "www.groogle.com")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "www.groogle.com")

    def test_img(self):
        node = TextNode("Alt text", TextType.IMAGE, "www.image.com/dogs.jpeg")
        html_node = text_node_to_html_node(node)

        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "www.image.com/dogs.jpeg")
        self.assertEqual(html_node.props["alt"], "Alt text")


if __name__ == "__main__":
    unittest.main()