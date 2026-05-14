import unittest
from blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "### Introduction\nWelcome to our project documentation.\n\nThis project uses Python and Bootstatic.\n\n### Features\n* Easy to use\n* Fast generation\n* Flexible templates\n* Markdown support\n\n### Installation\nRun `pip install bootstatic`.\n"
        expected = [
            "### Introduction\nWelcome to our project documentation.",
            "This project uses Python and Bootstatic.",
            "### Features\n* Easy to use\n* Fast generation\n* Flexible templates\n* Markdown support",
            "### Installation\nRun `pip install bootstatic`."
        ]
        self.assertEqual(markdown_to_blocks(markdown), expected)
    
    def test_markdown_to_blocks_complex(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


class TestBlockType(unittest.TestCase):
    def test_block_type(self):
        self.assertEqual(block_to_block_type("### Introduction"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("Welcome to our project documentation."), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("- Easy to use\n- Fast generation\n- Flexible templates\n- Markdown support"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Easy to use\n2. Fast generation\n3. Flexible templates\n4. Markdown support"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("> Easy to use\n> Fast generation\n> Flexible templates\n> Markdown support"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("```python\nprint('Hello, world!')\n```"), BlockType.CODE)

if __name__ == '__main__':
    unittest.main()
