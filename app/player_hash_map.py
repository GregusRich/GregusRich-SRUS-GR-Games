from app.player_list import PlayerList
from app.player import Player

class PlayerHashMap:
    """A hash map that stores player data, using PlayerList to handle collisions."""
    SIZE: int = 10

    def __init__(self):
        """Initialises a hash map with a list of player instances."""
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]

    def get_index(self, key: str) -> int:
        """Returns player's index in the hash map.

        Args:
            key (str): The player's UID.

        Returns:
            int: The index in the hash map.
        """
        return Player.pearson_hash(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
        """Adds a new player or updates an existing player's name in the hash map.

        Args:
            key (str): The uid of the player.
            name (str): The player's name.
        """
        index = self.get_index(key)
        player_list = self.hashmap[index]
        new_player = Player(key, name)
        player_list.add_or_update_player(new_player)

    def __getitem__(self, key: str) -> Player:
        """Gets a player based off it's key.
        Args:
            key (str): The uid of the player.

        Returns: The player
        """
        index = self.get_index(key)
        player_list = self.hashmap[index]
        return player_list.get_player_by_uid(key)

    def __delitem__(self, key: str) -> None:
        """Deleted a player based off it's key."""
        index = self.get_index(key)
        player_list = self.hashmap[index]
        try:
            player_list.delete_player_by_uid(key)
        except ValueError:
            raise KeyError(f"Player with UID '{key}' not found.")

    def __len__(self) -> int:
        """Returns the total number of players in the hash map."""
        total = 0
        for player_list in self.hashmap:
            current_node = player_list.head
            while current_node:
                total += 1
                current_node = current_node.next_node
        return total

    def display(self) -> None:
        """Displays the content of each PlayerList with one or more players. Prints the index of the PlayerList"""
        for index, player_list in enumerate(self.hashmap):
            if player_list: # Change to: if not player_list.is_empty(): To view only indexes with players in them.
                print(f"Index {index}:")
                player_list.display()
                print("-" * 20)