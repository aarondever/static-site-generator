import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_for_none_props(self) -> None:
        node = HTMLNode()
        expected = ""
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_one_props(self) -> None:
        node = HTMLNode(props={"href": "https://www.google.com"})
        expected = 'href="https://www.google.com"'
        self.assertEqual(expected, node.props_to_html())

    def test_props_to_html_for_two_props(self) -> None:
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, node.props_to_html())


if __name__ == "__main__":
    unittest.main()
