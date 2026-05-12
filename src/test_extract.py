import unittest

from extract import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is a ![alt text](image.jpg)"
        expected = [("alt text", "image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_markdown_images_multiple(self):
        text = "This is a ![alt text](image.jpg) and ![alt text](image2.jpg)"
        expected = [("alt text", "image.jpg"), ("alt text", "image2.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_with_spaces(self):
        text = "This is a ![alt text](image with spaces.jpg)"
        expected = [("alt text", "image with spaces.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_markdown_images_with_special_chars(self):
        text = "This is a ![alt text](image!@#$.jpg)"
        expected = [("alt text", "image!@#$.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_markdown_images_with_no_images(self):
        text = "This is a text node"
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        text = "This is a [alt text](link.jpg)"
        expected = [("alt text", "link.jpg")]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_extract_markdown_links_multiple(self):
        text = "This is a [alt text](link.jpg) and [alt text](link2.jpg)"
        expected = [("alt text", "link.jpg"), ("alt text", "link2.jpg")]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_extract_markdown_links_with_spaces(self):
        text = "This is a [alt text](link with spaces.jpg)"
        expected = [("alt text", "link with spaces.jpg")]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_extract_markdown_links_with_special_chars(self):
        text = "This is a [alt text](link!@#$.jpg)"
        expected = [("alt text", "link!@#$.jpg")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_markdown_links_with_no_links(self):
        text = "This is a text node"
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)