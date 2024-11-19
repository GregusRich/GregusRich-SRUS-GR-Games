from app.player import Player

class PlayerBNode:
    """A class that represents a node in the BST, containing a Player object. """

    def __init__(self, player: Player):
        """Initialises a node with the given Player object.

        Args:
            player (Player): The Player object to be stored in this node.
        """
        self._player = player
        self._left = None # Left child
        self._right = None # Right child

    @property
    def player(self) -> Player:
        """Returns the Player object stored in this node. """
        return self._player

    @player.setter
    def player(self, player: Player):
        """Sets the Player object for this node.

        Args:
            player (Player): The new Player object to be stored.
        """
        self._player = player

    @property
    def left(self):
        """Returns the left child node (subtree). """
        return self._left

    @left.setter
    def left(self, node):
        """Sets the left child node (subtree).

        Args:
            node (PlayerBNode): The node to be set as the left child.
        """
        self._left = node

    @property
    def right(self):
        """Returns the right child node (subtree). """
        return self._right

    @right.setter
    def right(self, node):
        """Sets the right child node (subtree).

        Args:
            node (PlayerBNode): The node to be set as the right child.
        """
        self._right = node