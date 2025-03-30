import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("One node", TextType.NORMAL)
        node2 = TextNode("Another node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("Same", TextType.NORMAL, "www.abc.com")
        node2 = TextNode("Same", TextType.NORMAL, "www.abd.com")

if __name__ == "__main__":
    unittest.main()