import unittest

from leafnode import LeafNode, text_node_to_html_node
from textnode import TextNode, TextNodeType

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

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextNodeType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold node", TextNodeType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextNodeType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextNodeType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextNodeType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props["href"], "https://www.boot.dev")
        self.assertEqual(html_node.value, "This is a link node")

    def test_image(self):
        node = TextNode("This is an image node", TextNodeType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://www.boot.dev")
        self.assertEqual(html_node.props["alt"], "This is an image node")
    
    def test_invalid_text_node_type(self):
        node = TextNode("This is an invalid text node type", "invalid")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)