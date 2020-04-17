import unittest
from v1.node import Node


class TestNode(unittest.TestCase):

    def test_node(self):
        node = Node()

        self.assertIsNone(node.next)

        value = "100"
        node.next = value
        self.assertEqual(value, node.next)
