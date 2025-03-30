import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_single_prop(self):
        node = HTMLNode(props={"key":"value"})

        self.assertEqual(node.props_to_html(), " key=value")
    
    def test_multi_props(self):
        node = HTMLNode(props={"key1":"value1", "key2":"value2", "key3":"value3"})

        self.assertEqual(node.props_to_html(), " key1=value1 key2=value2 key3=value3")
    
    def test_props_none(self):
        node = HTMLNode()

        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")

        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Hello, world!")

        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()