import unittest
from app.player_list import PlayerList
from app.player import Player

"""
Unit tests for the player_list class.
"""

class PlayerTestList(unittest.TestCase):
    def test_append_node_to_empty_list(self):
        player_list = PlayerList()
        player = Player("12345", "Greg")
        player_list.append_node(player)
        self.assertEqual(player_list._head.player.uid, "12345")
        self.assertEqual(player_list._head.player.name, "Greg")
        self.assertIsNone(player_list._head.next_node)
