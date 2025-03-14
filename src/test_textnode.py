import unittest

from nodes.text_node import TextNode, TextType


class TestTextNode(unittest.TestCase):

    def test_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        self.assertEqual(node, node2)

    def test_not_eq(self) -> None:
        node = TextNode("This is a text node", TextType.BOLD, "http://github.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        self.assertNotEqual(node, node2)

    def test_diff_text_type(self) -> None:
        node = TextNode("This is a text node", TextType.ITALIC, "https://github.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        self.assertNotEqual(node, node2)

    def test_diff_text(self) -> None:
        node = TextNode("This is a text", TextType.BOLD, "https://github.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://github.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_lingk(self):
        node = TextNode("This is a link node", TextType.LINK, "https://github.com")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://github.com"})

    def test_image(self):
        node = TextNode("this is an image", TextType.IMAGE, "https://image.png")
        html_node = node.to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props, {"src": "https://image.png", "alt": "this is an image"}
        )

    def test_invalid_text_type(self):
        node = TextNode("Invalid node", "invalid")
        with self.assertRaises(ValueError):
            node.to_html_node()


if __name__ == "__main__":
    unittest.main()
