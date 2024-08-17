class Player:
    """
    A class that represents a player.

    Attributes:
    unique_id (str): a unique identifier for the player.
    player_name (str): the name of the player.
    """
    def __init__(self, unique_id: str, player_name: str):
        """
        Initialises the player object with a unique id and a player name.

        :param unique_id: the unique identifier of the player.
        :param player_name: the name of the player.
        """
        self._unique_id: str = unique_id
        self._player_name: str = player_name

    @property
    def uid(self) -> str:
        """
        :return: the unique id of the player
        :rtype: string
        """
        return self._unique_id

    @property
    def name(self) -> str:
        """
        :return: the name of the player.
        :rtype: string
        """
        return self._player_name

    def __str__(self) -> str:
        """
        :return: A human-readable string representation of the player object.
        :rtype: string
        """
        return f"Player: uid={self._unique_id}, name={self._player_name}"
