import random


class Player:
    """
    A class that represents a player.

    Attributes:
    unique_id (str): a unique identifier for the player.
    player_name (str): the name of the player.
    """
    def __init__(self, unique_id: str, player_name: str):
        """
        Initialises the player object with a unique id and a player name.
        """
        self._unique_id: str = unique_id
        self._player_name: str = player_name

    _pearson_table = list(range(256))
    random.seed(42)
    random.shuffle(_pearson_table)

    @classmethod
    def pearson_hash(cls, key: str) -> int:
        """Hashes the player UID string and returns an int which will be the index for that player (node).

        Args:
            key (str): The string to hash.

        Returns:
            int: The hash value between 0 and SIZE - 1.
        """
        hash_ = 0
        for char in key:
            hash_ = cls._pearson_table[hash_ ^ ord(char)]
        return hash_

    def __hash__(self):
        """Returns the hash of the player's UID."""
        return self.pearson_hash(self.uid)

    @property
    def uid(self) -> str:
        """
        Returns: The uid of the player.
        """
        return self._unique_id

    @property
    def name(self) -> str:
        """
        Returns: The name of the player.
        """
        return self._player_name

    @name.setter
    def name(self, new_name: str):
        """Sets a new name for the player.

        Args:
            new_name (str): The new name for the player.
        """
        self._player_name = new_name

    def __str__(self) -> str:
        """Returns a human-readable string representation of the player object."""
        return f"Player: uid={self._unique_id}, name={self._player_name}"

    def __eq__(self, other):
        """Compares two players. Two players returning the same hash should be considered equal"""
        return isinstance(other, Player) and self.uid == other.uid
