from app.player_node import PlayerNode

class PlayerList:
    """
    A class to represents a list of players
    """
    _head = PlayerNode | None

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

        """
        To append a node at the head of the list we need to:
        1. [Done] Make a new node with the value
        2. [Done] Make function to check if the head reference is empty, return or raise exception
        3. [Done] If it's empty, set the head to reference itself 
        4. [Done] Otherwise make the new nodes next reference the head node (inserts it at the start) 
        """

    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if the list is empty, False otherwise.
        :rtype: bool
        """
        return self._head is None
