import unittest
from app.player import Player

class TestPlayerSorting(unittest.TestCase):
    def test_sort_players(self):
        player1 = Player("12345", "Greg")
        player2 = Player("654321", "Karen")
        player3 = Player("5555555", "Simon")
        player4 = Player("987654", "Tom")

        # Assigning scores
        player1.score = 10
        player2.score = 15
        player3.score = 10
        player4.score = 20

        players = [player1, player2, player3, player4]
        expected_order = [player4, player2, player1, player3]

        # Sort the players
        sorted_players = Player.sort_players(players)

        # Check if the sorted list matches the expected order
        self.assertEqual(sorted_players, expected_order)

        # Verify that the scores are in descending order
        for i in range(len(sorted_players) - 1):
            self.assertTrue(sorted_players[i].score >= sorted_players[i + 1].score)

    def test_sort_players_with_equal_scores(self):
        # Players with equal scores
        player1 = Player("111", "Billy")
        player2 = Player("222", "Sally")
        player3 = Player("333", "Bobby")
        player4 = Player("444", "Robby")

        # Assigning equal scores
        player1.score = 15
        player2.score = 15
        player3.score = 15
        player4.score = 15

        players = [player3, player1, player4, player2]
        expected_order = [player3, player1, player4, player2]

        # Sort the players
        sorted_players = Player.sort_players(players)

        # Since all scores are equal, the order should remain the same
        self.assertEqual(sorted_players, expected_order)

    def test_sort_empty_list(self):
        players = []
        expected_order = []

        # Sort the empty list
        sorted_players = Player.sort_players(players)

        # The sorted list should be empty
        self.assertEqual(sorted_players, expected_order)

    def test_sort_single_player(self):
        player = Player("12345", "Greg")
        player.score = 10
        players = [player]
        expected_order = [player]

        # Sort the list with a single player
        sorted_players = Player.sort_players(players)

        # The sorted list should be the same as the input list
        self.assertEqual(sorted_players, expected_order)
