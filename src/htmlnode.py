class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list | None = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HTMLNode):
            return NotImplemented
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode('{self.tag}', '{self.value}', {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def _props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html
    