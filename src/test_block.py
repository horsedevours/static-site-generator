import unittest
from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):

    def test_paragraph(self):
        blockType = block_to_block_type("This is a normal paragraph of text.\nNothing special about it.")

        self.assertEqual(BlockType.PARAGRAPH, blockType)

    def test_code(self):
        blockType = block_to_block_type("```This is a block of amazing code.\nIT IS!```")

        self.assertEqual(BlockType.CODE, blockType)

    def test_heading(self):
        blockType = block_to_block_type("### HERE'S A HEADING FOR YA")

        self.assertEqual(BlockType.HEADING, blockType)

    def test_bad_heading(self):
        blockType = block_to_block_type("###HERE'S A HEADING FOR YA")

        self.assertEqual(BlockType.PARAGRAPH, blockType)
    
    def test_too_many_heading(self):
        blockType = block_to_block_type("######## HERE'S A HEADING FOR YA")

        self.assertEqual(BlockType.PARAGRAPH, blockType)

    def test_ordered_list(self):
        blockType = block_to_block_type("1. Get some ham\n2. Smell all over the place\n3. Fall asleep")

        self.assertEqual(BlockType.O_LIST, blockType)
    
    def test_bad_ordered_list(self):
        blockType = block_to_block_type("4. Get some ham\n2. Smell all over the place")

        self.assertEqual(BlockType.PARAGRAPH, blockType)

    def test_quote(self):
        blockType = block_to_block_type(">I'm quoting the most important things.\n>All for your edification!\n> - John Cowsong")

        self.assertEqual(BlockType.QUOTE, blockType)

    def test_unordered_list(self):
        blockType = block_to_block_type("- Sometimes I don't fall down\n- I heard a dog and a bird \n - There are many types of birds over there")

        self.assertEqual(BlockType.U_LIST, blockType)