import unittest
from app.player import Player
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode

class TestPlayerBST(unittest.TestCase):
    """Unit tests for the PlayerBST class."""

    # region Insertion Tests
    def setUp(self):
        """Set up the test case with a BST and some players."""
        self.bst = PlayerBST()
        self.player1 = Player("1", "Greg")
        self.player2 = Player("2", "Tim")
        self.player3 = Player("3", "Billy")
        self.player4 = Player("4", "Bobby")
        self.player5 = Player("5", "Robby")

    def test_insert_single_node(self):
        """Test inserting a single node into the BST."""
        self.bst.insert(self.player1)
        self.assertIsNotNone(self.bst.root)
        self.assertEqual(self.bst.root.player.name, "Greg")

    def test_insert_multiple_nodes(self):
        """Test inserting multiple nodes into the BST."""
        self.bst.insert(self.player3)  # Billy
        self.bst.insert(self.player1)  # Greg
        self.bst.insert(self.player4)  # Bobby
        self.bst.insert(self.player2)  # Tim
        self.bst.insert(self.player5)  # Robby

        # In-order traversal should return players in alphabetical order
        players_in_order = self.bst.in_order_traversal()
        expected_names = ["Billy", "Bobby", "Greg", "Robby", "Tim"]
        actual_names = [player.name for player in players_in_order]
        self.assertEqual(actual_names, expected_names)

    def test_insert_duplicate_node(self):
        """Test inserting a duplicate node updates the existing node's player."""
        self.bst.insert(self.player1)
        self.assertEqual(self.bst.root.player.name, "Greg")
        # Create a new Player with the same name but different UID
        updated_player = Player("6", "Greg")
        self.bst.insert(updated_player)
        self.assertEqual(self.bst.root.player.uid, "6")
        self.assertEqual(self.bst.root.player.name, "Greg")

    def test_structure_of_bst(self):
        """Test the structure of the BST after insertions."""
        # Insert players in a specific order to create a known tree structure
        self.bst.insert(self.player3)  # Billy
        self.bst.insert(self.player1)  # Greg
        self.bst.insert(self.player5)  # Robby
        self.bst.insert(self.player4)  # Bobby
        self.bst.insert(self.player2)  # Tim

        # Now check that the structure is as expected
        # Root should be Billy
        self.assertEqual(self.bst.root.player.name, "Billy")
        # Left child of root should be None (since no names are less than "Billy")
        self.assertIsNone(self.bst.root.left)
        # Right child of root should be Greg
        self.assertEqual(self.bst.root.right.player.name, "Greg")
        # Left child of Greg should be Bobby
        self.assertEqual(self.bst.root.right.left.player.name, "Bobby")
        # Right child of Greg should be Robby
        self.assertEqual(self.bst.root.right.right.player.name, "Robby")
        # Right child of Robby should be Tim
        self.assertEqual(self.bst.root.right.right.right.player.name, "Tim")
    # endregion

    # region Searching Tests
    def test_search_existing_player(self):
        """Test searching for an existing player in the BST. """

        # Insert players into the BST
        self.bst.insert(self.player1)
        self.bst.insert(self.player2)
        self.bst.insert(self.player3)
        self.bst.insert(self.player4)
        self.bst.insert(self.player5)

        # Search for an existing player
        result = self.bst.search("Greg")
        self.assertIsNotNone(result)
        self.assertEqual(result.uid, "1")
        self.assertEqual(result.name, "Greg")

    def test_search_nonexistent_player(self):
        """Test searching for a player that does not exist in the BST."""
        # Insert some players
        self.bst.insert(self.player1)  # Greg
        self.bst.insert(self.player3)  # Billy

        # Search for a player not in the BST
        result = self.bst.search("Tim")  # Not inserted yet
        self.assertIsNone(result)

    def test_search_in_empty_tree(self):
        """Test searching in an empty BST."""
        # BST is empty
        result = self.bst.search("Greg")
        self.assertIsNone(result)

    def test_search_after_updating_player(self):
        """Test searching for a player after updating the node with a duplicate name."""
        # Insert a player
        self.bst.insert(self.player1)  # Greg

        # Update the player with the same name but different UID
        updated_player = Player("6", "Greg")
        self.bst.insert(updated_player)

        # Search for the player
        result = self.bst.search("Greg")
        self.assertIsNotNone(result)
        self.assertEqual(result.uid, "6")
        self.assertEqual(result.name, "Greg")
    # endregion


if __name__ == '__main__':
    unittest.main()
