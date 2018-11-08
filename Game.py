import Infos


class Game(object):
    _infos = []
    _size = 19
    _has_started = False
    _turn_counter = 0
    _first_to_play = False
    _board = []

    def __init__(self, size):
        self._size = size
        self._infos = Infos.Infos
        self.reinitialize_game()

    def infos(self, value):
        if value is not None:
            self._infos = value
        return self._infos

    def has_started(self, value):
        if value is not None:
            self._has_started = value
        return self._has_started

    def increment_turn_counter(self):
        self._turn_counter += 1
        return self._turn_counter

    def decrement_turn_counter(self):
        self._turn_counter -= 1
        return self._turn_counter

    def turn_counter(self):
        return self._turn_counter

    def first_to_play(self, value):
        if value is not None:
            self._first_to_play = value
        return self._first_to_play

    def board(self):
        return self._board

    def reinitialize_game(self):
        self._has_started = False
        self._turn_counter = 0
        self._first_to_play = False
        self.reinitialize_board()

    def reinitialize_board(self):
        self._board = [[0 for x in range(self._size)] for y in range(self._size)]

    def is_first_turn(self):
        return self._turn_counter == 0 or (self._turn_counter == 1 and not self._first_to_play)

    def set_info_value(self, key, value):
        dictionary = {
            "timeout_turn": self._infos.timeout_turn,
            "timeout_match": self._infos.timeout_match,
            "max_memory": self._infos.max_memory,
            "time_left": self._infos.time_left,
            "game_type": self._infos.game_type,
            "rule": self._infos.rule,
            "evaluate": self._infos.evaluate,
            "folder": self._infos.folder,
        }
        info = dictionary.get(key)
        if info is not None:
            info(self._infos, value)

    def place_stone(self, x, y, who):
        self.increment_turn_counter()
        self._board[x][y] = who
