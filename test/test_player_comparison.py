import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode
from app.player_hash_map import PlayerHashMap

class TestPlayerComparison(unittest.TestCase):
    def setUp(self):
        # Using the same players as in your previous tests
        self.player1 = Player("12345", "Greg")
        self.player2 = Player("654321", "Karen")
        self.player3 = Player("5555555", "Simon")
        self.player4 = Player("987654", "Tom")

        # Assigning scores
        self.player1.score = 10
        self.player2.score = 15
        self.player3.score = 10
        self.player4.score = 20

    def test_eq(self):
        # Players with the same score should be equal
        self.assertTrue(self.player1 == self.player3)
        self.assertFalse(self.player1 == self.player2)

    def test_ne(self):
        # Players with different scores should not be equal
        self.assertTrue(self.player1 != self.player2)
        self.assertFalse(self.player1 != self.player3)

    def test_lt(self):
        # Less than comparison based on score
        self.assertTrue(self.player1 < self.player2)
        self.assertFalse(self.player2 < self.player1)

    def test_le(self):
        # Less than or equal to comparison based on score
        self.assertTrue(self.player1 <= self.player2)
        self.assertTrue(self.player1 <= self.player3)
        self.assertFalse(self.player2 <= self.player1)

    def test_gt(self):
        # Greater than comparison based on score
        self.assertTrue(self.player4 > self.player2)
        self.assertFalse(self.player1 > self.player3)

    def test_ge(self):
        # Greater than or equal to comparison based on score
        self.assertTrue(self.player4 >= self.player2)
        self.assertTrue(self.player1 >= self.player3)
        self.assertFalse(self.player1 >= self.player4)

if __name__ == '__main__':
    unittest.main()
