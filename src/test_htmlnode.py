import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_for_none_props(self) -> None:
        node = HTMLNode()
        expected = ""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_one_props(self) -> None:
        node = HTMLNode(props={"href": "https://www.google.com"})
        expected = ' href="https://www.google.com"'
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_two_props(self) -> None:
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())


class TestLeafNode(unittest.TestCase):

    def test_to_html_for_no_tag(self) -> None:
        node = LeafNode(None, value="no tag value")
        expected = "no tag value"
        self.assertEqual(expected, node.to_html())

    def test_to_html_for_tag_no_props(self) -> None:
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(expected, node.to_html())

    def test_to_html_for_tag_props(self) -> None:
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(expected, node.to_html())


if __name__ == "__main__":
    unittest.main()
