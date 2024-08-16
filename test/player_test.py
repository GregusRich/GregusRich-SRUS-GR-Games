import unittest
from app.player import Player

"""
Unit tests for the player class.
"""


class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        player = Player("12345", "Greg")
        player2 = Player("987654", "Tom")
        self.assertEqual(player.uid, "12345")
        self.assertEqual(player2.uid, "987654")

    def test_name_property(self):
        player = Player("12345", "Greg")
        player2 = Player("987654", "Tom")
        self.assertEqual(player.name, "Greg")
        self.assertEqual(player2.name, "Tom")

