import unittest

from main import extract_title

class TestMain(unittest.TestCase):

    def test_extract_title(self):
        markdown = """
Some text for no reason
# Here is the header     
Something else
"""

        title = extract_title(markdown)
        self.assertEqual("Here is the header", title)