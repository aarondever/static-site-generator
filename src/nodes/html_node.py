from collections.abc import Mapping, Sequence
from typing import Optional, Self


class HTMLNode:

    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[Sequence[Self]] = None,
        props: Optional[Mapping[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        return " " + " ".join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self) -> str:
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
