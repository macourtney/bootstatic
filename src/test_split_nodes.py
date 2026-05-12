import unittest

from textnode import TextNode, TextNodeType
from split_nodes import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        nodes = [TextNode("This is **text node**, **not bold**", TextNodeType.TEXT)]
        delimiter = "**"
        text_type = TextNodeType.BOLD
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.BOLD),
            TextNode(", ", TextNodeType.TEXT),
            TextNode("not bold", TextNodeType.BOLD)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, delimiter, text_type), expected)

    def test_split_nodes_italics(self):
        nodes = [TextNode("This is _text node_ and not bold.", TextNodeType.TEXT)]
        delimiter = "_"
        text_type = TextNodeType.ITALIC
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.ITALIC),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, delimiter, text_type), expected)

    def test_split_nodes_code(self):
        nodes = [TextNode("This is text node and `code`.", TextNodeType.TEXT)]
        delimiter = "`"
        text_type = TextNodeType.CODE
        expected = [
            TextNode("This is text node and ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),
            TextNode(".", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, delimiter, text_type), expected)

    def test_split_nodes_unclosed_delimiter(self):
        nodes = [TextNode("This is text node and `code.", TextNodeType.TEXT)]
        delimiter = "`"
        text_type = TextNodeType.CODE
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, delimiter, text_type)

    def test_split_nodes_multiple_delimiters(self):
        nodes = [
            TextNode("This is **text node**, **not bold** and `code`.", TextNodeType.TEXT),
            TextNode("More text", TextNodeType.TEXT)
        ]
        delimiter = "**"
        text_type = TextNodeType.BOLD
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.BOLD),
            TextNode(", ", TextNodeType.TEXT),
            TextNode("not bold", TextNodeType.BOLD),
            TextNode(" and `code`.", TextNodeType.TEXT),
            TextNode("More text", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, delimiter, text_type), expected)
