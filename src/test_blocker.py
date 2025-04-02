import unittest
from blocker import markdown_to_blocks

class TestBlocker(unittest.TestCase):

    def test_markdown_to_blocks(self):
        blocks = markdown_to_blocks("# This is a heading\n\nThis is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n- This is the first list item in a list block\n- This is a list item\n- This is another list item")

        self.assertListEqual(["# This is a heading", "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.", "- This is the first list item in a list block\n- This is a list item\n- This is another list item"], blocks)

    def test_excessive_newlines(self):
        blocks = markdown_to_blocks("# This is a heading\n\n\n\n\n\nThis is a paragraph of text.")
        

        self.assertListEqual(["# This is a heading", "This is a paragraph of text."], blocks)