import unittest

from htmlnode import HTMLNode

class TextHtmlNode(unittest.TestCase):
    def test_p(self):
        node_1 = HTMLNode(None,None,None,{"href": "https://www.google.com",
    "target": "_blank"}).props_to_html()
        node_2 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node_1, node_2)

    def test_no_props(self):
        node_1 = HTMLNode(None,None,None,None).props_to_html()
        node_2 = ""
        self.assertEqual(node_1, node_2)

    def test_empty_props(self):
        node_1 = HTMLNode(None,None,None,{}).props_to_html()
        node_2 = ""
        self.assertEqual(node_1, node_2)

if __name__ == "__main__":
    unittest.main()