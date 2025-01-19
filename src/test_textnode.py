import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
