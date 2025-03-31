import unittest

from splitter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitter(unittest.TestCase):

    def test_bold(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
