import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    """Unit tests for the player class.

    Tests included:
        - Testing that the player uid is properly set
        - Testing that the player name is properly set
    """
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
