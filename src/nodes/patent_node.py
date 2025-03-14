from collections.abc import Mapping, Sequence

from .html_node import HTMLNode


class ParentNode(HTMLNode):

    def __init__(
        self,
        tag: str,
        children: Sequence[HTMLNode],
        props: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(tag=tag, children=children, props=props)  # type: ignore

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Tag is required.")

        if not self.children:
            raise ValueError("Children is required.")

        inner_html = ""

        for child in self.children:
            inner_html += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"
