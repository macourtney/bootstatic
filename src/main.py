from textnode import TextNode, TextNodeType


def main():
    tnode1 = TextNode("This is some anchor text", TextNodeType.LINK, "https://www.boot.dev")
    return tnode1

if __name__ == "__main__":
    print(main())