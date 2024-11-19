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
        self._score: int = 0
    
    _pearson_table = list(range(256))
    random.seed(42)
    random.shuffle(_pearson_table)

    @staticmethod
    def pearson_hash(key: str) -> int:
        """Hashes the player UID string and returns an int which will be the index for that player (node). """
        hash_ = 0
        for char in key:
            hash_ = Player._pearson_table[hash_ ^ ord(char)]
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

    @property
    def score(self) -> int:
        """
        Returns: The score of the player.
        """
        return self._score

    @score.setter
    def score(self, new_score: int):
        """ Sets the new score for the player.

        Args:
            new_score (int): The new score of the player
        """
        if not isinstance(new_score, int) or new_score < 0:
            raise ValueError("Score must be a positive integer.")
        self._score = new_score

    def __str__(self) -> str:
        """Returns a human-readable string representation of the player object."""
        return f"Player: uid={self._unique_id}, name={self._player_name}"

    def __eq__(self, other):
        """Compares two players. Two players returning the same hash should be considered equal"""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score == other.score

    def __ne__(self, other):
        """Checks if two players have different scores."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score != other.score

    def __lt__(self, other):
        """Checks if this player's score is less than another's."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score < other.score

    def __le__(self, other):
        """Checks if this player's score is less than or equal to another's."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score <= other.score

    def __gt__(self, other):
        """Checks if this player's score is greater than another's."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score > other.score

    def __ge__(self, other):
        """Checks if this player's score is greater than or equal to another's."""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score >= other.score

    @staticmethod
    def sort_players(players: list) -> list:
        """Sorts a list of Player objects in descending order based on their scores using selection sort.

        Args:
            players (list): The list of Player objects to sort.

        Returns:
            list: The sorted list of Player objects.
        """
        n = len(players)
        for i in range(n):
            # Assume the max is the first element
            max_idx = i
            for j in range(i + 1, n):
                if players[j].score > players[max_idx].score:
                    max_idx = j
            # Swap the found maximum element with the first element
            players[i], players[max_idx] = players[max_idx], players[i]
        return players
