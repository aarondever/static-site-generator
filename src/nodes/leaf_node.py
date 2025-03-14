from collections.abc import Mapping
from typing import Optional

from .html_node import HTMLNode


class LeafNode(HTMLNode):

    def __init__(
        self, tag: Optional[str], value: str, props: Mapping[str, str] | None = None
    ) -> None:
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:

        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
