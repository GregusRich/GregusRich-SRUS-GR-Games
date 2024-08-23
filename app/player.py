class Player:
    """
    A class that represents a player.

    Attributes:
    uid (str): a unique identifier for the player.
    player_name (str): the name of the player.
    """
    def __init__(self, uid: str, player_name: str):
        """
        Initialises the player object with a unique id and a player name.

        :param uid: the unique identifier of the player.
        :param player_name: the name of the player.
        """
        self._uid: str = uid  # rename to uid
        self._player_name: str = player_name  # -> name

    @property
    def uid(self) -> str:
        """
        :return: the unique id of the player
        :rtype: string
        """
        return self._uid

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
        return f"Player: uid={self._uid}, name={self._player_name}"
