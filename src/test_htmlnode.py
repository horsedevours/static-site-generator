import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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
        node = LeafNode(None, "Hello, world!")

        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_child_with_many_children(self):
        child1 = LeafNode("span", "A span")
        child2 = LeafNode("p", "A paragraph")
        child3 = LeafNode("h1", "A header")
        parent_node = ParentNode("div", [child1, child2, child3])

        self.assertEqual(
            parent_node.to_html(),
            "<div><span>A span</span><p>A paragraph</p><h1>A header</h1></div>"
        )

if __name__ == "__main__":
    unittest.main()