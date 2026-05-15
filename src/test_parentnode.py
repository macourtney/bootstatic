from blocks import BlockType
from parentnode import block_type_to_html_node
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

class TestBlockTypeToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        node = block_type_to_html_node(BlockType.PARAGRAPH, "This is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.children[0].value, "This is a paragraph")
    
    def test_heading(self):
        node = block_type_to_html_node(BlockType.HEADING, "# This is a heading")
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.children[0].value, "This is a heading")
    
    def test_unordered_list(self):
        node = block_type_to_html_node(BlockType.UNORDERED_LIST, "- This is an unordered list")
        self.assertEqual(node.tag, "ul")
        self.assertEqual(len(node.children), 1)
        child = node.children[0]
        self.assertEqual(child.tag, "li")
        self.assertEqual(len(child.children), 1)
        self.assertEqual(child.children[0].value, "This is an unordered list")
    
    def test_ordered_list(self):
        node = block_type_to_html_node(BlockType.ORDERED_LIST, "1. This is an ordered list")
        self.assertEqual(node.tag, "ol")
        self.assertEqual(len(node.children), 1)
        child = node.children[0]
        self.assertEqual(child.tag, "li")
        self.assertEqual(len(child.children), 1)
        self.assertEqual(child.children[0].value, "This is an ordered list")
    
    def test_quote(self):
        node = block_type_to_html_node(BlockType.QUOTE, "> This is a quote")
        self.assertEqual(node.tag, "blockquote")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "This is a quote")
    
    def test_code(self):
        node = block_type_to_html_node(BlockType.CODE, "```This is a code```")
        self.assertEqual(node.tag, "pre")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].tag, "code")
        self.assertEqual(node.children[0].value, "This is a code")
