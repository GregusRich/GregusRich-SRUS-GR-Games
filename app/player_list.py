from app.player_node import PlayerNode


class PlayerList:
    """
    A class to represents a list of players
    """
    _head = PlayerNode | None # The head is of type Player Node or None (if list is empty).

    def __init__(self, _player_node: PlayerNode | None = None):
        self._head = None  # Initialise the head of the list to None.

    """
    Inserts a node at the head of the list
    """
    def append_node(self, value: any) -> None:
        new_node = PlayerNode(value)  # Creates a new node with the value passed in
        if self.is_empty():
            self._head = new_node # If the list is empty, the new node becomes the head node
        else:
            # If the list is not empty, insert the new node at the head
            new_node.next_node = self._head # Sets the new nodes next_node reference to the head node
            self._head = new_node # Sets the new nodes head reference to itself, thus becoming the head node

    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if the list is empty, False otherwise.
        :rtype: bool
        """
        return self._head is None
