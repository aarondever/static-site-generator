import unittest

from nodes import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_tag(self):
        child_node = LeafNode(None, "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()


if __name__ == "__main__":
    unittest.main()
