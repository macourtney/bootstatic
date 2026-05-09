import unittest

from textnode import TextNode, TextNodeType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.BOLD)
        self.assertEqual(node, node2)
    
    def test_ne(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_ne_url(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a text node", TextNodeType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_ne_text(self):
        node = TextNode("This is a text node", TextNodeType.BOLD)
        node2 = TextNode("This is a different text node", TextNodeType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()