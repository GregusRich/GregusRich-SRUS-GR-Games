import unittest
from app.player_list import PlayerList
from app.player import Player

"""
Unit tests for the player_list class.

Tests included:
    - Appending a node to an empty list (node should become the head node)
    - Appending a node to a list that is not empty
    - If the list is empty the head is None
    - That the head references are correctly replaced when appending a new node
"""


class TestPlayerList(unittest.TestCase):
    # Test appending a node to an empty list and that the node should become the head node.
    def test_append_node_to_empty_list(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player_list.append_node(player1)
        self.assertEqual(player_list._head.player.uid, "12345")
        self.assertEqual(player_list._head.player.name, "Greg")
        self.assertIsNone(player_list._head.next_node)  # Since there's only one node, next_node should be None

    # Test appending a node to a list that is not empty
    def test_append_node_to_none_empty_list(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player3 = Player("5555555", "Simon")
        player_list.append_node(player1)
        player_list.append_node(player2)
        player_list.append_node(player3)

        # player3 "Simon" should be at the head now as it was appended last
        self.assertEqual(player_list._head.player.uid, "5555555")
        self.assertEqual(player_list._head.player.name, "Simon")

        # player2 "Tom" should be next
        self.assertEqual(player_list._head.next_node.player.uid, "654321")
        self.assertEqual(player_list._head.next_node.player.name, "Tom")

        # player1 "Greg" should be last
        self.assertEqual(player_list._head.next_node.next_node.player.uid, "12345")
        self.assertEqual(player_list._head.next_node.next_node.player.name, "Greg")

        # Last node's next_node should be None
        self.assertIsNone(player_list._head.next_node.next_node.next_node)

    # Test that the list is empty when nothing is added and the head is None.
    def test_empty_list(self):
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty())
        self.assertIsNone(player_list._head)

    # Test that the head references are correctly replaced when appending a new node.
    def test_head_replacement(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player_list.append_node(player1)
        self.assertEqual(player_list._head.player.uid, "12345")
        player_list.append_node(player2)
        self.assertEqual(player_list._head.player.uid, "654321")