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