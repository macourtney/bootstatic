from htmlnode import HTMLNode

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
