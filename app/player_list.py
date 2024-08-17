from app.player_node import PlayerNode
from app.player import Player

class PlayerList:
    """
    A class to represents a list of players
    """
    _head = PlayerNode | None # The head is of type Player Node or None (if list is empty)
    _tail = PlayerNode | None # If list is empty both the head and tail are None

    def __init__(self, _player_node: PlayerNode | None = None):
        self._head = None # Initialise the head of the list to None
        self._tail = None # Initialise the tail of the list to None

    @property
    def head(self) -> PlayerNode | None:
        """
        :return: The head node of the list.
        """
        return self._head

    @head.setter
    def head(self, _player_node: PlayerNode | None):
        """
        Set the head node of the list.

        :param node: The node to set as the head.
        """
        self._head = _player_node

    @property
    def tail(self) -> PlayerNode | None:
        """
        :return: The tail node of the list.
        """
        return self._tail

    @tail.setter
    def tail(self, _player_node: PlayerNode | None):
        """
        Set the tail node of the list.

        :param _player_node: The node to set as tail
        :return:
        """
        self._tail = _player_node

    """
    Inserts a node at the head of the list
    """

    def append_node_to_head(self, value: any) -> None:
        new_node = PlayerNode(value)  # Creates a new node with the value passed in
        if self.is_empty():
            """
            If the list is empty, the new node becomes both the head and the tail node
            """
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, insert the new node at the head
            new_node.next_node = self.head  # Set the new node's next_node to the current head
            self.head.previous_node = new_node  # Set the current head's previous_node to the new node
            self.head = new_node  # Update the head to the new node

    """
    Insert a node at the tail of the list
    
    Notes: By having a reference to the tail node, this allows appending to the tail in constant time 0(1), 
    instead of having to traverse the entire list like in a singly linked list O(n) (linear time). 
    p.s Thanks for the in class explanation and graphs! 
    """
    def append_node_to_tail(self, value: any) -> None:
        new_node = PlayerNode(value)
        if self.is_empty():
            """
            If the list is empty, the new node becomes both the head and the tail node
            """
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node # Update the current tail to point to the new node
            new_node.previous_node = self.tail # Update the new node's previous pointer to point to the old tail
            self.tail = new_node # Update the tail to the new node

    """
    Deletes the head node in the list
    """
    def delete_head(self) -> None:
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        if self.head == self.tail:
            # Only one node in the list
            self.head = None
            self.tail = None
        else:
            # Move head to the next node
            self.head = self.head.next_node
            if self.head:
                self.head.previous_node = None

    """
    Deletes the tail node in the list
    """
    def delete_tail(self) -> None:
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list.")
        if self.head == self.tail:
            # Only one node in the list
            self.head = None
            self.tail = None
        else:
            # Move tail to the previous node
            self.tail = self.tail.previous_node
            if self.tail:
                self.tail.next_node = None

    """
    Deletes a node by it's key. 
    """
    def delete_by_key(self, key: str) -> None:
        current = self.head

        while current is not None:
            """
            Traverses the list and removes the node by key, 
            also taking into account if the node is the head or tail node.
            """
            if current.key == key:
                if current == self.head: # If the node is the head
                    self.head = current.next_node
                    if self.head:
                        self.head.previous_node = None
                    else:
                        self.tail = None  # If the list is now empty, reset the tail

                # If the node is the tail
                elif current == self.tail:
                    self.tail = current.previous_node
                    if self.tail:
                        self.tail.next_node = None

                # If the node isn't the head or tail then update the references to remove it.
                else:
                    current.previous_node.next_node = current.next_node
                    current.next_node.previous_node = current.previous_node
                return

            current = current.next_node  # Move to the next node

        raise ValueError(f"Node with key {key} not found.")


    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if the list is empty, False otherwise.
        :rtype: bool
        """
        return self._head is None and self._tail is None

    """
    Displays the entire list from head to tail
    """
    def display(self, forward: bool = True) -> None:
        """
        Displays the entire list from head to tail if forward is True,
        or from tail to head if forward is False.

        :param forward: Direction in which to display the list. Default is True (head to tail).
        """
        if self.is_empty():
            print("The list is empty.")
            return

        if forward:
            current_node = self.head
            while current_node:
                print(current_node)
                current_node = current_node.next_node
        else:
            current_node = self.tail
            while current_node:
                print(current_node)
                current_node = current_node.previous_node
