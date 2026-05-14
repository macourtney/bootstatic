from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    QUOTE = "quote"
    CODE = "code"

def markdown_to_blocks(markdown):
    blocks = []
    for line in markdown.split('\n\n'):
        stripped_line = line.strip()
        if stripped_line:
            blocks.append(stripped_line)
    return blocks

def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if re.match("^#{1,6}", block):
        return BlockType.HEADING
    if multiline_block_to_block_type(block, "^- "):
        return BlockType.UNORDERED_LIST
    if multiline_block_to_block_type(block, "^\\d+\\. "):
        return BlockType.ORDERED_LIST
    if multiline_block_to_block_type(block, "^>"):
        return BlockType.QUOTE
    return BlockType.PARAGRAPH

def multiline_block_to_block_type(block, start_expression):
    lines = block.split('\n')
    for line in lines:
        if not re.match(start_expression, line):
            return False
    return True

    
