import unittest
from app.player_hash_map import PlayerHashMap

class TestHashMap(unittest.TestCase):
    """ Unit tests for testing the Hash Map functionality. Tests include:

        test_add_and_retrieve_players
        test_update_player
        test_delete_player
        test_length
        test_collision_handling
        test_nonexistent_player
    """
    def setUp(self):
        # Add players
        self.hash_map = PlayerHashMap()
        self.hash_map['09724'] = 'Greg'   # Hashes to index 1
        self.hash_map['67890'] = 'Tom'    # Hashes to index 6
        self.hash_map['54321'] = 'Billy'  # Hashes to index 1
        self.hash_map['09876'] = 'Bobby'  # Hashes to index 2
        self.hash_map['11223'] = 'Simon'  # Hashes to index 3
        self.hash_map['12345'] = 'Karen'  # Hashes to index 0
        self.hash_map['12456'] = 'Jill'   # Hashes to index 9
        self.hash_map['12567'] = 'Lauren' # Hashes to index 0
        self.hash_map['20130'] = 'Maddy'  # Hashes to index 3

    def test_add_and_retrieve_players(self):
        # Retrieve players and check names
        self.assertEqual(self.hash_map['09724'].name, 'Greg')
        self.assertEqual(self.hash_map['67890'].name, 'Tom')
        self.assertEqual(self.hash_map['54321'].name, 'Billy')
        self.assertEqual(self.hash_map['09876'].name, 'Bobby')
        self.assertEqual(self.hash_map['11223'].name, 'Simon')
        self.assertEqual(self.hash_map['12345'].name, 'Karen')
        self.assertEqual(self.hash_map['12456'].name, 'Jill')
        self.assertEqual(self.hash_map['12567'].name, 'Lauren')
        self.assertEqual(self.hash_map['20130'].name, 'Maddy')

    def test_update_player(self):
        # Update a player's name and check
        self.hash_map['09724'] = 'Gregory'
        self.assertEqual(self.hash_map['09724'].name, 'Gregory')

    def test_delete_player(self):
        # Delete a player and check that they are removed
        del self.hash_map['67890']
        with self.assertRaises(KeyError):
            _ = self.hash_map['67890']

    def test_length(self):
        # Check the length of the hash map
        self.assertEqual(len(self.hash_map), 9)
        del self.hash_map['54321']
        self.assertEqual(len(self.hash_map), 8)

    def test_collision_handling(self):
        # Players that hash to the same index
        # '09724' and '54321' both hash to index 1
        index1 = self.hash_map.get_index('09724')
        index2 = self.hash_map.get_index('54321')
        self.assertEqual(index1, index2)
        player_list = self.hash_map.hashmap[index1]
        uids_in_list = []
        current_node = player_list.head
        while current_node:
            uids_in_list.append(current_node.player.uid)
            current_node = current_node.next_node
        self.assertIn('09724', uids_in_list)
        self.assertIn('54321', uids_in_list)

    def test_nonexistent_player(self):
        # Try to retrieve a player that doesn't exist
        with self.assertRaises(KeyError):
            _ = self.hash_map['99999']
