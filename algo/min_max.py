from algo import peril
from algo import attack


def begin(board):
    size = len(board[0])
    axe = [0, 0, 0]
    y = int(size / 2)
    x = int(size / 2)
    if board[y][x] == 0:
        axe[0] = y
        axe[1] = x
        axe[2] = 1
    elif board[y + 1][x] == 0:
        axe[0] = y + 1
        axe[1] = x
        axe[2] = 1
    elif board[y - 1][x] == 0:
        axe[0] = y - 1
        axe[1] = x
        axe[2] = 1
    return axe


def my_turn(board):
    is_win = peril.is_win(board, 1)
    if is_win[2] > 0:
        return -1
    alarm = peril.check_alarm(board, 2)
    if alarm[2] > 0:
        return 1
    punch = attack.get_attack(board, 1)
    if punch[2] > 0:
        board[punch[0], punch[1]] = 1
        return enemy_turn(board)


def enemy_turn(board):
    res = [0, 0, 0]
    is_win = peril.is_win(board, 2)
    if is_win[2] > 0:
        res[0] = is_win[0]
        res[1] = is_win[1]
        res[2] = -1
    alarm = peril.check_alarm(board, 1)
    if alarm[2] > 0:
        res[0] = alarm[0]
        res[1] = alarm[1]
        res[2] = 1
        return res
    punch = attack.get_attack(board, 1)
    if punch[2] > 0:
        res[0] = punch[0]
        res[1] = punch[1]
        return res
    return res


def AI_brain(board):
    is_win = peril.is_win(board, 1)
    if is_win[2] > 0:
        return [is_win[0], is_win[1]]
    alarm = peril.check_alarm(board, 2)
    if alarm[2] > 0:
        return [alarm[0], alarm[1]]
    punch = attack.get_attack(board, 1)
    if punch[2] > 0:
        return [punch[0], punch[1]]
    return enemy_turn(board)


def min_max(game):
    board = game.board()
    if game.is_first_turn():
        axe = begin(board)
    else:
        axe = AI_brain(board)
    cp_board = board
    cp_board[axe[0]][axe[1]] = 1
    validation = enemy_turn(cp_board)
    if validation[2] == -1:
        axe[0] = validation[0]
        axe[1] = validation[1]
    return axe
