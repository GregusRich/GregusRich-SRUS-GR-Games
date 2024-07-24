class PlayerNode:
    """
    A class that represents a player node in a doubly linked list of players.
    """
    def __init__(self, player):
        """
        Initialise a player node with pointers to the next and previous node.

        :param player: Represents a player object.
        """
        self._player = player
        self._next = None  # a pointer to the next node
        self._previous = None  # a pointer to the previous node

    @property
    def player(self):
        """
        :return: the player object.
        """
        return self._player

    @property
    def next(self):
        """
        :return: the player next node.
        """
        return self._next

    @next.setter
    def next(self, next_node):
        """
        Sets the next node.

        :param next_node: the next node of the player object.
        :type next_node: PlayerNode
        """
        self._next = next_node

    @property
    def previous(self):
        """
        :return: the player previous node.
        """
        return self._previous

    @previous.setter
    def previous(self, previous_node):
        """
        Sets the previous node.

        :param previous_node: the previous node of the player object.
        :type previous_node: PlayerNode
        """
        self._previous = previous_node

    @property
    def key(self):
        """
        :return: the unique id of the player.
        """
        return self._player.uid

    def __str__(self) -> str:
        """
        :return: a human-readable string of the node object.
        :rtype: string
        """
        return f"Node: player={self._player}, previous node={self._previous.uid}, next node={self._next.uid}"
