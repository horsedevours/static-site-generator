import unittest

from htmler import markdown_to_html_node

class TestHTMLer(unittest.TestCase):

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_heading(self):
        md = """
    #### This is a proper heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>This is a proper heading</h4></div>"
        )
    
    def test_ordered_list(self):
        md = """
    1. Step one
    2. Step two [and away](https://www.groogle.com)
    3. Step three
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Step one</li><li>Step two <a href=https://www.groogle.com>and away</a></li><li>Step three</li></ol></div>"
        )

    def test_quote(self):
        md = """
>Axe what you can do for
>your county.
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Axe what you can do for\nyour county.</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- I like dogs
- I like steak
- I think about carpeting
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>I like dogs</li><li>I like steak</li><li>I think about carpeting</li></ul></div>"
        )