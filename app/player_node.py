from app.player import Player


class PlayerNode:
    """
    A class that represents a player node in a doubly linked list of players.
    """

    def __init__(self, player: Player):
        """
        Initialise a player node with pointers to the next_node and previous_node.

        :param player: Represents a player object.
        """
        self._player = player
        self._next_node = None  # A pointer to the next node
        self._previous_node = None  # A pointer to the previous node

    @property
    def player(self) -> Player:
        return self._player

    @property
    def next_node(self):
        """
        :return: The next node in the list, or None if there is no next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, next_node) -> None:
        """
        Sets the next node.
        """
        self._next_node = next_node

    @property
    def previous_node(self):
        """
        :return: The previous node in the list, or None if there is no previous node.
        """
        return self._previous_node

    @previous_node.setter
    def previous_node(self, previous_node) -> None:
        """
        Sets the previous node.
        """
        self._previous_node = previous_node

    @property
    def key(self) -> str:
        return self._player.uid

    def __str__(self) -> str:
        prev_uid = self._previous_node.key if self._previous_node else "None"
        next_uid = self._next_node.key if self._next_node else "None"
        return f"Node: player={self._player}, previous_node uid={prev_uid}, next_node uid={next_uid}"
