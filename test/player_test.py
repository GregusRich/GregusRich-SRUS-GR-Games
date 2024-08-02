import unittest
from app.player import Player

"""
Unit tests for the player class.
"""


class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        player = Player("12345", "Greg")
        player2 = Player(unique_id="987654", player_name="Tom")
        self.assertEqual(player.uid, "12345")
        self.assertEqual(player2.uid, second="987654")

    def test_name_property(self):
        player = Player("12345", "Greg")
        player2 = Player(unique_id="987654", player_name="Tom")
        self.assertEqual(player.name, "Greg")
        self.assertEqual(player2.name, second="Tom")

