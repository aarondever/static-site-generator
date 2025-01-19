from textnode import TextNode, TextType


def main() -> None:
    text_node = TextNode("h1", TextType.NORMAL, "http://google.com")
    print(text_node)


main()
