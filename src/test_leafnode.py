import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "bold"})
        self.assertEqual(node.to_html(), '<p class="bold">Hello, world!</p>')
    
    def test_leaf_to_html_p_with_multiple_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "bold", "id": "1"})
        self.assertEqual(node.to_html(), '<p class="bold" id="1">Hello, world!</p>')
    
    def test_leaf_to_html_p_with_many_props(self):
        node = LeafNode("p", "Hello, world!", {"class": "bold", "id": "1", "style": "color: red"})
        self.assertEqual(node.to_html(), '<p class="bold" id="1" style="color: red">Hello, world!</p>')
    
    def test_leaf_to_html_p_with_no_props(self):
        node = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')
    
    def test_leaf_to_html_p_with_no_props_explicitly(self):
        node = LeafNode("p", "Hello, world!", None)
        self.assertEqual(node.to_html(), '<p>Hello, world!</p>')
    
    def test_leaf_to_html_p_with_none_value(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()
    
    def test_leaf_to_html_p_with_none_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_p_with_none_tag_and_none_props(self):
        node = LeafNode(None, "Hello, world!", None)
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_p_with_none_tag_and_props(self):
        node = LeafNode(None, "Hello, world!", {"class": "bold"})
        self.assertEqual(node.to_html(), "Hello, world!")