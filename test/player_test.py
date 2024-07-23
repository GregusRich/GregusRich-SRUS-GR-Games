import unittest
from app.player import Player

"""
Unit tests for the player class.
"""


class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        player = Player("12345", "Greg")
        self.assertEqual(player.uid, "12345")

    def test_name_property(self):
        player = Player("12345", "Greg")
        self.assertEqual(player.name, "Greg")
