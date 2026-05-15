from leafnode import LeafNode, text_node_to_html_node
from split_nodes import text_to_textnodes
import re
from htmlnode import HTMLNode
from blocks import BlockType

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict | None = None):
        self.tag = tag
        self.children = children
        self.props = props
        self.value = None
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"ParentNode('{self.tag}', {self.children}, {self.props})"
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self._props_to_html()}>{children_html}</{self.tag}>"
    
    def _props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html

def add_leaves(text: str):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children

def block_type_to_html_node(block_type: BlockType, block: str):
    if block_type == BlockType.PARAGRAPH:
        block = " ".join(block.split("\n"))
        return ParentNode("p", add_leaves(block))
    elif block_type == BlockType.HEADING:
        level = len(re.match("^#{1,6}", block).group())
        return ParentNode(f"h{level}", add_leaves(block[level+1:]))
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split('\n')
        li_nodes = []
        for line in lines:
            li_nodes.append(ParentNode("li", add_leaves(line[2:])))
        return ParentNode("ul", li_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split('\n')
        li_nodes = []
        for line in lines:
            li_nodes.append(ParentNode("li", add_leaves(line[3:])))
        return ParentNode("ol", li_nodes)
    elif block_type == BlockType.QUOTE:
        lines = block.split('\n')
        quote_nodes = []
        for line in lines:
            quote_nodes.extend(add_leaves(line[2:]))
        return ParentNode("blockquote", quote_nodes)
    elif block_type == BlockType.CODE:
        return ParentNode("pre", [LeafNode("code", block[3:-3])])
