import Game
from algo import min_max


def ia_move(game):
    axe = min_max.min_max(game)
    game.place_stone(axe[0], axe[1], 1)
    print(str(axe[0]) + "," + str(axe[1]))


def brain_start(msg, game):
    size = int(msg[1])
    if size < 0 or game.has_started(None):
        print("ERROR")
    else:
        game = Game.Game(size)
        print("OK")
    return game


def brain_restart(msg, game):
    game.reinitialize_game()
    print("OK")
    return game


def brain_rectstart(msg, game):
    print("ERROR")
    return game


def brain_turn(msg, game):
    if not game.has_started(None):
        game.has_started(True)
        game.first_to_play(False)
    moves = msg[1].split(",")
    game.place_stone(int(moves[0]), int(moves[1]), 2)
    ia_move(game)
    return game


def brain_begin(msg, game):
    if not game.has_started(None):
        game.has_started(True)
        game.first_to_play(True)
        ia_move(game)
    return game


def brain_board(msg, game):
    msg = input()
    while msg != "DONE":
        moves = msg.split(",")
        game.place_stone(int(moves[0]), int(moves[1]), int(moves[2]))
        msg = input()
    ia_move(game)
    return game


def brain_takeback(msg, game):
    game.place_stone(int(msg[1]), int(msg[2]), 0)
    game.decrement_turn_counter()
    print("OK")
    return game


def brain_end(msg, game):
    return game


def brain_infos(msg, game):
    game.set_info_value(msg[1], msg[2])
    return game


def brain_about(msg, game):
    print("name=\"LazyBrain\", version=\"1.0\", author=\"MAA\", country=\"France\"")
    return game


def play():
    game = Game.Game(20)
    msg = input()
    msg = msg.split(" ")
    dictionary = {
        "START": brain_start,
        "RESTART": brain_restart,
        "RECTSTART": brain_rectstart,
        "TURN": brain_turn,
        "BEGIN": brain_begin,
        "BOARD": brain_board,
        "TAKEBACK": brain_takeback,
        "END": brain_end,
        "INFOS": brain_infos,
        "ABOUT": brain_about,
    }
    while msg[0] != "END":
        instruction = dictionary.get(msg[0])
        if instruction is not None:
            game = instruction(msg, game)
        msg = input()
        msg = msg.split(" ")


def main():
    play()


if __name__ == "__main__":
    main()
