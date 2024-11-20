from app.player import Player
from app.player_bnode import PlayerBNode


class PlayerBST:
    """A class that represents a Binary Search Tree (BST) for Player objects. """

    def __init__(self):
        """Initialises the BST with a root node set to None. """
        self._root = None

    @property
    def root(self):
        """Returns the root node of the BST. """
        return self._root

    @root.setter
    def root(self, node):
        """Sets the root node of the BST. """
        self._root = node

    def insert(self, player : Player):
        """Inserts a Player object into the BST using the player's name as the key. """
        if self._root is None:
            self._root = PlayerBNode(player)
        else:
            self._insert_recursive(self.root, player)

    def _insert_recursive(self, current_node: PlayerBNode, player: Player):
        """Recursively inserts a Player into the BST.

        Args:
            current_node (PlayerBNode): The current node being compared.
            player (Player): The Player object to insert.
        """
        if player.name < current_node.player.name: # This compares by alphabetical order
            if current_node.left is None:
                current_node.left = PlayerBNode(player)
            else:
                self._insert_recursive(current_node.left, player)
        elif player.name > current_node.player.name:
            if current_node.right is None:
                current_node.right = PlayerBNode(player)
            else:
                self._insert_recursive(current_node.right, player)
        else:
            # If there is a duplicate key, it updates the existing node's player
            current_node.player = player

    def in_order_traversal(self) -> list:
        """Performs an in-order traversal of the BST and returns a list of Player objects.

        Returns:
            list: A list of Player objects in in-order traversal.
        """
        players = []
        self._in_order_recursive(self.root, players)
        return players

    def _in_order_recursive(self, current_node: PlayerBNode, players: list):
        """Helper method to help test for in-order traversal.

        Args:
            current_node (PlayerBNode): The current node being traversed.
            players (list): The list to append the Player objects to.
        """
        if current_node is not None:
            self._in_order_recursive(current_node.left, players)
            players.append(current_node.player)
            self._in_order_recursive(current_node.right, players)
