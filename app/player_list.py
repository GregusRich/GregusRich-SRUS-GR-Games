from app.player_node import PlayerNode
from app.player import Player

class PlayerList:
    """A class to represents a list of players"""
    _head = PlayerNode | None # The head is of type Player Node or None (if list is empty)
    _tail = PlayerNode | None # If list is empty both the head and tail are None

    def __init__(self, node: PlayerNode | None = None):
        self._head = None # Initialise the head of the list to None
        self._tail = None # Initialise the tail of the list to None

    @property
    def head(self) -> PlayerNode | None:
        """Returns the head node of the list."""
        return self._head

    @head.setter
    def head(self, node: PlayerNode | None):
        """Set the head node of the list."""
        self._head = node

    @property
    def tail(self) -> PlayerNode | None:
        """Returns the tail node of the list."""
        return self._tail

    @tail.setter
    def tail(self, _player_node: PlayerNode | None):
        """Set the tail node of the list."""
        self._tail = _player_node

    def append_node_to_head(self, value: any) -> None:
        new_node = PlayerNode(value)  # Creates a new node with the value passed in
        if self.is_empty():
            """Inserts a node at the head of the list.
            
            If the list is empty, the new node becomes both the head and the tail node.
            """
            self.head = new_node
            self.tail = new_node
        else:
            # If the list is not empty, insert the new node at the head
            new_node.next_node = self.head  # Set the new node's next_node to the current head
            self.head.previous_node = new_node  # Set the current head's previous_node to the new node
            self.head = new_node  # Update the head to the new node

    def append_node_to_tail(self, value: any) -> None:
        """Insert a node at the tail of the list

        By having a reference to the tail node, this allows appending to the tail in constant time 0(1),
        instead of having to traverse the entire list like in a singly linked list O(n) (linear time).
        p.s Thanks for the in class explanation and graphs!
        """
        new_node = PlayerNode(value)
        if self.is_empty():
            # If the list is empty, the new node becomes both the head and the tail node"""
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node # Update the current tail to point to the new node
            new_node.previous_node = self.tail # Update the new node's previous pointer to point to the old tail
            self.tail = new_node # Update the tail to the new node

    def delete_head(self) -> None:
        """
        Deletes the head node in the list
        """
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

    def delete_tail(self) -> None:
        """
        Deletes the tail node in the list
        """
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

    def delete_by_key(self, key: str) -> None:
        """ Deletes a node by it's key"""
        current_node = self.head

        while current_node is not None:
            """Traverses the list and removes the node by key, 
            also taking into account if the node is the head or tail node."""
            if current_node.key == key:
                if current_node == self.head: # If the node is the head
                    self.head = current_node.next_node
                    if self.head:
                        self.head.previous_node = None
                    else:
                        self.tail = None  # If the list is now empty, reset the tail

                # If the node is the tail
                elif current_node == self.tail:
                    self.tail = current_node.previous_node
                    if self.tail:
                        self.tail.next_node = None

                # If the node isn't the head or tail then update the references to remove it.
                else:
                    current_node.previous_node.next_node = current_node.next_node
                    current_node.next_node.previous_node = current_node.previous_node
                return

            current_node = current_node.next_node  # Move to the next node

        raise ValueError(f"Node with key {key} not found.")

    def is_empty(self) -> bool:
        """
        Check if the list is empty.

        :return: True if the list is empty, False otherwise.
        :rtype: bool
        """
        return self._head is None and self._tail is None

    def add_or_update_player(self, player: Player) -> None:
        """Adds a new player to the list or updates the player's name if they already exist."""
        current_node = self.head
        while current_node:
            if current_node.player.uid == player.uid:
                current_node.player._player_name = player.name
                return
            current_node = current_node.next_node
        self.append_node_to_tail(player)

    def get_player_by_uid(self, uid: str) -> Player:
        """Retrieves a player from the list based on their UID.

        Args:
            uid (str): The UID of the player.

        Returns:
            The player with the matching UID.
        """
        current_node = self.head
        while current_node:
            if current_node.player.uid == uid:
                return current_node.player
            current_node = current_node.next_node
        raise KeyError(f"Player with UID '{uid}' not found.")

    def delete_player_by_uid(self, uid: str) -> None:
        """Deletes a player from the list based on their UID.

        Args:
            uid (str): The UID of the player to delete.
        """
        self.delete_by_key(uid)

    def display(self, forward: bool = True) -> None:
        """Displays the players in the list.

        :Args
            forward (bool): Direction in which to display the list. True will print head to tail.
        """
        if self.is_empty():
            print("  (No players)")
            return

        players = []
        if forward:
            current_node = self.head
            while current_node:
                players.append(str(current_node))
                current_node = current_node.next_node
        else:
            current_node = self.tail
            while current_node:
                players.append(str(current_node))
                current_node = current_node.previous_node

        print("  " + "   (linked node-->)   ".join(players))