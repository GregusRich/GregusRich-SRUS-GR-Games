from app.player_list import PlayerList
from app.player import Player
from app.player_hash_map import PlayerHashMap
from test.test_hash_map import TestHashMap

def main():
    player_hash_map = PlayerHashMap()
    # Add players
    player_hash_map['09724'] = 'Greg'
    player_hash_map['67890'] = 'Tom'
    player_hash_map['54321'] = 'Billy'
    player_hash_map['09876'] = 'Bobby'
    player_hash_map['11223'] = 'Simon'
    player_hash_map['12345'] = 'Karen'
    player_hash_map['12456'] = 'Jill'
    player_hash_map['12567'] = 'Lauren'
    player_hash_map['20130'] = 'Maddy'

    # Display the hash map
    player_hash_map.display()

if __name__ == "__main__":
    main()


    """Previous code for testing adding players to the player list.
    # Create the PlayerList
    player_list = PlayerList()

    # Add some players to the list
    player1 = Player("12345", "Greg")
    player2 = Player("654321", "Tom")
    player3 = Player("987654", "Simon")

    # Append nodes to the list
    player_list.append_node_to_head(player1)  # Greg is now the head
    player_list.append_node_to_tail(player2)  # Tom is now the tail
    player_list.append_node_to_tail(player3)  # Simon is now the tail

    # Display the list from head to tail
    print("Displaying from head to tail:")
    player_list.display()  # Should print Greg, Tom, Simon in order

    # Display the list from tail to head
    print("\nDisplaying from tail to head:")
    player_list.display(forward=False)  # Should print Simon, Tom, Greg in order
    """
