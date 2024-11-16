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
    - Appending a node to an empty list at the tail (node should become the tail node)
    - Appending a node to a list that is not empty at the tail
    - That the tail references are correctly replaced when appending a new node
"""


class TestPlayerList(unittest.TestCase):

    # Test appending a node to an empty list and that the node should become the head node.
    def test_append_node_to_empty_list(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player_list.append_node_to_head(player1)
        self.assertEqual(player_list._head.player.uid, "12345")
        self.assertEqual(player_list._head.player.name, "Greg")
        self.assertIsNone(player_list._head.next_node)  # Since there's only one node, next_node should be None

    # Test appending a node to a list that is not empty
    def test_append_node_to_none_empty_list(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player3 = Player("5555555", "Simon")
        player_list.append_node_to_head(player1)
        player_list.append_node_to_head(player2)
        player_list.append_node_to_head(player3)

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
        player_list.append_node_to_head(player1)
        self.assertEqual(player_list._head.player.uid, "12345")
        player_list.append_node_to_head(player2)
        self.assertEqual(player_list._head.player.uid, "654321")

    # Test appending a node to an empty list and that the node should become the tail node.
    def test_append_node_to_empty_tail(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player_list.append_node_to_tail(player1)
        self.assertEqual(player_list.tail.player.uid, "12345")
        self.assertEqual(player_list.tail.player.name, "Greg")
        self.assertIsNone(player_list.tail.previous_node)  # Since there's only one node, previous_node should be None

    # Test appending a node to a list that is not empty at the tail
    def test_append_node_to_non_empty_tail(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player3 = Player("5555555", "Simon")
        player_list.append_node_to_tail(player1)
        player_list.append_node_to_tail(player2)
        player_list.append_node_to_tail(player3)

        # player1 "Greg" should be at the head since it was added first
        self.assertEqual(player_list.head.player.uid, "12345")
        self.assertEqual(player_list.head.player.name, "Greg")

        # player3 "Simon" should be at the tail now as it was appended last
        self.assertEqual(player_list.tail.player.uid, "5555555")
        self.assertEqual(player_list.tail.player.name, "Simon")

        # player2 "Tom" should be between player1 and player3
        self.assertEqual(player_list.head.next_node.player.uid, "654321")
        self.assertEqual(player_list.tail.previous_node.player.uid, "654321")

    # Test that the tail references are correctly replaced when appending a new node.
    def test_tail_replacement(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player_list.append_node_to_tail(player1)
        self.assertEqual(player_list.tail.player.uid, "12345")

    # Test deleting the head node from the list
    def test_delete_head(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player_list.append_node_to_head(player1)
        player_list.append_node_to_head(player2)

        # Delete head (Tom should be removed, Greg should be the new head)
        player_list.delete_head()
        self.assertEqual(player_list.head.player.uid, "12345")
        self.assertIsNone(player_list.head.previous_node)

        # Delete head again (Greg should be removed, list should be empty)
        player_list.delete_head()
        self.assertTrue(player_list.is_empty())

    # Test deleting the tail node from the list
    def test_delete_tail(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player_list.append_node_to_tail(player1)
        player_list.append_node_to_tail(player2)

        # Delete tail (Tom should be removed, Greg should be the new tail)
        player_list.delete_tail()
        self.assertEqual(player_list.tail.player.uid, "12345")
        self.assertIsNone(player_list.tail.next_node)

        # Delete tail again (Greg should be removed, list should be empty)
        player_list.delete_tail()
        self.assertTrue(player_list.is_empty())

    # Test deleting a node by key (regardless of position)
    def test_delete_node_by_key(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player3 = Player("987654", "Simon")
        player_list.append_node_to_head(player1)
        player_list.append_node_to_tail(player2)
        player_list.append_node_to_tail(player3)

        # Delete the middle node (Tom)
        player_list.delete_by_key("654321")
        self.assertEqual(player_list.head.player.uid, "12345")
        self.assertEqual(player_list.tail.player.uid, "987654")

        # The head's next node's previous node should point back to the head
        self.assertEqual(player_list.head.next_node.previous_node, player_list.head)

        # The tail's previous node's next node should point forward to the tail
        self.assertEqual(player_list.tail.previous_node.next_node, player_list.tail)

        # Delete the head node (Greg)
        player_list.delete_by_key("12345")
        self.assertEqual(player_list.head.player.uid, "987654")
        self.assertIsNone(player_list.head.previous_node)
        self.assertIsNone(player_list.head.next_node)

        # Delete the tail node (Simon), which is now the only node left
        player_list.delete_by_key("987654")
        self.assertTrue(player_list.is_empty())
        self.assertIsNone(player_list.head)
        self.assertIsNone(player_list.tail)

    # Test attempting to delete a non-existent node by key
    def test_delete_non_existent_node(self):
        player_list = PlayerList()
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Tom")
        player_list.append_node_to_head(player1)
        player_list.append_node_to_tail(player2)

        # Try deleting a non-existent node
        with self.assertRaises(ValueError):
            player_list.delete_by_key("999999")

if __name__ == '__main__':
    unittest.main()