import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        node2 = HTMLNode("p", "Hello world", [], {"class": "bold"})
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        node2 = HTMLNode("p", "Hello world", [], {"class": "italic"})
        self.assertNotEqual(node, node2)
    
    def test_ne_text(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        node2 = HTMLNode("p", "Goodbye world", [], {"class": "bold"})
        self.assertNotEqual(node, node2)
    
    def test_ne_children(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        node2 = HTMLNode("p", "Hello world", [HTMLNode("b", "Hello world")], {"class": "bold"})
        self.assertNotEqual(node, node2)
    
    def test_ne_props(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        node2 = HTMLNode("p", "Hello world", [], {"class": "bold", "id": "bold"})
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold"})
        self.assertEqual(repr(node), "HTMLNode('p', 'Hello world', [], {'class': 'bold'})")

    def test_props_to_html(self):
        node = HTMLNode("p", "Hello world", [], {"class": "bold", "id": "bold"})
        self.assertEqual(node._props_to_html(), ' class="bold" id="bold"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello world", [], {})
        self.assertEqual(node._props_to_html(), '')

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Hello world", [], None)
        self.assertEqual(node._props_to_html(), '')
    