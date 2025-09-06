import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_bold(self):
        node_1 = TextNode("This is a text node", TextType.BOLD)
        node_2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node_1, node_2)

    def test_eq_italic(self):
        node_1 = TextNode("This is another text node", TextType.ITALIC)
        node_2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertEqual(node_1, node_2)
    
    def test_not_eq_link(self):
        node_1 = TextNode("This is a link", TextType.LINK)
        node_2 = TextNode("This is another link", TextType.LINK)
        self.assertNotEqual(node_1, node_2)
    
    def test_not_eq_types(self):
        node_1 = TextNode("This is another text node", TextType.BOLD)
        node_2 = TextNode("This is another text node", TextType.ITALIC)
        self.assertNotEqual(node_1, node_2)



if __name__ == "__main__":
    unittest.main()