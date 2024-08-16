class PlayerNode:
    """
    A class that represents a player node in a doubly linked list of players.
    """
    def __init__(self, player):
        """
        Initialise a player node with pointers to the next_node and previous_node node.

        :param player: Represents a player object.
        """
        self._player = player
        self._next_node = None  # a pointer to the next_node node
        self._previous_node = None  # a pointer to the previous_node node

    @property
    def player(self):
        """
        :return: the player object.
        """
        return self._player

    @property
    def next_node(self):
        """
        :return: the player next_node node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        Sets the next_node node.

        :param next_node: the next_node of the player object.
        :type next_node: PlayerNode
        """
        self._next_node = next_node

    @property
    def previous_node(self):
        """
        :return: the player previous_node node.
        """
        return self._previous_node

    @previous_node.setter
    def previous_node(self, previous_node):
        """
        Sets the previous_node node.

        :param previous_node: the previous_node node of the player object.
        :type previous_node: PlayerNode
        """
        self._previous_node = previous_node

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
        prev_uid = self._previous_node.uid if self._previous_node else "None"
        next_uid = self._next_node.uid if self._next_node else "None"
        return f"Node: player={self._player}, previous_node uid={prev_uid}, next_node uid={next_uid}"
