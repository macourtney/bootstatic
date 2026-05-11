import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_to_html_div(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p></div>")
    
    def test_parent_to_html_div_with_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], {"class": "bold"})
        self.assertEqual(node.to_html(), '<div class="bold"><p>Hello, world!</p></div>')
    
    def test_parent_to_html_div_with_multiple_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], {"class": "bold", "id": "1"})
        self.assertEqual(node.to_html(), '<div class="bold" id="1"><p>Hello, world!</p></div>')
    
    def test_parent_to_html_div_with_many_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], {"class": "bold", "id": "1", "style": "color: red"})
        self.assertEqual(node.to_html(), '<div class="bold" id="1" style="color: red"><p>Hello, world!</p></div>')
    
    def test_parent_to_html_div_with_no_props(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], {})
        self.assertEqual(node.to_html(), '<div><p>Hello, world!</p></div>')
    
    def test_parent_to_html_div_with_no_props_explicitly(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!")], None)
        self.assertEqual(node.to_html(), '<div><p>Hello, world!</p></div>')
    
    def test_parent_to_html_div_with_none_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_to_html_div_with_none_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_to_html_div_with_none_tag_and_none_props(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")], None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parent_to_html_div_with_none_tag_and_props(self):
        node = ParentNode(None, [LeafNode("p", "Hello, world!")], {"class": "bold"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_to_html_div_with_multiple_children(self):
        node = ParentNode("div", [LeafNode("p", "Hello, world!"), LeafNode("p", "Hello, world!")])
        self.assertEqual(node.to_html(), "<div><p>Hello, world!</p><p>Hello, world!</p></div>")