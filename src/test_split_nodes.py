import unittest

from textnode import TextNode, TextNodeType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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
    


class TestSplitNodesImage(unittest.TestCase):
    def test_split_nodes_image(self):
        nodes = [TextNode("This is ![image](https://i.imgur.com/zjjcJKZ.png) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("image", TextNodeType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes), expected)
    
    def test_split_nodes_image_multiple(self):
        nodes = [TextNode("This is ![alt text](url) and ![alt text](url).", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("alt text", TextNodeType.IMAGE, "url"),
            TextNode(" and ", TextNodeType.TEXT),
            TextNode("alt text", TextNodeType.IMAGE, "url"),
            TextNode(".", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes), expected)
    
    def test_split_nodes_image_with_spaces(self):
        nodes = [TextNode("This is ![alt text](url with spaces) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("alt text", TextNodeType.IMAGE, "url with spaces"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes), expected)
    
    def test_split_nodes_image_with_special_chars(self):
        nodes = [TextNode("This is ![alt text](url!@#$) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("alt text", TextNodeType.IMAGE, "url!@#$"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_image(nodes), expected)
    
    def test_split_nodes_image_with_no_image(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), expected)

    def test_split_nodes_image_with_no_image_many_nodes(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("More text", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("More text", TextNodeType.TEXT)]
        self.assertEqual(split_nodes_image(nodes), expected)

    def test_split_nodes_image_with_no_image_many_nodes_with_image(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("![alt text](url)", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("alt text", TextNodeType.IMAGE, "url")]
        self.assertEqual(split_nodes_image(nodes), expected)


class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        nodes = [TextNode("This is [link text](url) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("link text", TextNodeType.LINK, "url"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes), expected)

    def test_split_nodes_link_multiple(self):
        nodes = [TextNode("This is [link text](url) and [link text](url).", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("link text", TextNodeType.LINK, "url"),
            TextNode(" and ", TextNodeType.TEXT),
            TextNode("link text", TextNodeType.LINK, "url"),
            TextNode(".", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes), expected)
    
    def test_split_nodes_link_with_spaces(self):
        nodes = [TextNode("This is [link text](url with spaces) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("link text", TextNodeType.LINK, "url with spaces"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes), expected)
    
    def test_split_nodes_link_with_special_chars(self):
        nodes = [TextNode("This is [link text](url!@#$) and not bold.", TextNodeType.TEXT)]
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("link text", TextNodeType.LINK, "url!@#$"),
            TextNode(" and not bold.", TextNodeType.TEXT)
        ]
        self.assertEqual(split_nodes_link(nodes), expected)
    
    def test_split_nodes_link_with_no_link(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT)]
        self.assertEqual(split_nodes_link(nodes), expected)

    def test_split_nodes_link_with_no_link_many_nodes(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("More text", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("More text", TextNodeType.TEXT)]
        self.assertEqual(split_nodes_link(nodes), expected)

    def test_split_nodes_link_with_no_link_many_nodes_with_link(self):
        nodes = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("[link text](url)", TextNodeType.TEXT)]
        expected = [TextNode("This is text node and not bold.", TextNodeType.TEXT), TextNode("link text", TextNodeType.LINK, "url")]
        self.assertEqual(split_nodes_link(nodes), expected)

class TestTextToTextnodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text node**, **not bold** and `code`."
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.BOLD),
            TextNode(", ", TextNodeType.TEXT),
            TextNode("not bold", TextNodeType.BOLD),
            TextNode(" and ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),
            TextNode(".", TextNodeType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_text_to_textnodes_multiple(self):
        text = "This is **text node**, **not bold** and `code`. More text"
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.BOLD),
            TextNode(", ", TextNodeType.TEXT),
            TextNode("not bold", TextNodeType.BOLD),
            TextNode(" and ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),
            TextNode(". More text", TextNodeType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_text_to_textnodes_multiple_delimiters(self):
        text = "This is **text node**, **not bold** and `code`. ![image](url)"
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text node", TextNodeType.BOLD),
            TextNode(", ", TextNodeType.TEXT),
            TextNode("not bold", TextNodeType.BOLD),
            TextNode(" and ", TextNodeType.TEXT),
            TextNode("code", TextNodeType.CODE),
            TextNode(". ", TextNodeType.TEXT),
            TextNode("image", TextNodeType.IMAGE, "url")
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_text_to_textnodes_complex(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextNodeType.TEXT),
            TextNode("text", TextNodeType.BOLD),
            TextNode(" with an ", TextNodeType.TEXT),
            TextNode("italic", TextNodeType.ITALIC),
            TextNode(" word and a ", TextNodeType.TEXT),
            TextNode("code block", TextNodeType.CODE),
            TextNode(" and an ", TextNodeType.TEXT),
            TextNode("obi wan image", TextNodeType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextNodeType.TEXT),
            TextNode("link", TextNodeType.LINK, "https://boot.dev")
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    

    def test_text_to_textnodes_empty(self):
        text = ""
        expected = [TextNode("", TextNodeType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)
