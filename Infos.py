class Infos(object):
    _timeout_turn = 0
    _timeout_match = 0
    _max_memory = 0
    _time_left = -1
    _game_type = 2
    _rule = 2
    _evaluate = [-1, -1]
    _folder = ""

    def timeout_turn(self, value):
        if value is not None:
            self._timeout_turn = value
        return self._timeout_turn

    def timeout_match(self, value):
        if value is not None:
            self._timeout_match = value
        return self._timeout_match

    def max_memory(self, value):
        if value is not None:
            self._max_memory = value
        return self._max_memory

    def time_left(self, value):
        if value is not None:
            self._time_left = value
        return self._time_left

    def game_type(self, value):
        if value is not None:
            self._game_type = value
        return self._game_type

    def rule(self, value):
        if value is not None:
            self._rule = value
        return self._rule

    def evaluate(self, value):
        if value is not None:
            self._evaluate = value
        return self._evaluate

    def folder(self, value):
        if value is not None:
            self._folder = value
        return self._folder

