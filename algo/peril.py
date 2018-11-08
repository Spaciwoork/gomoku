from algo import get_nb_match_pawn
from algo import min_max

def dang_diagonal_left(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if ((y - 1 >= 0 and y + 4 < size) and (x - 1 >= 0 and x + 4 < size)) and \
            (board[y - 1][x - 1] == 0 and board[y + 4][x + 4] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 2][x + 2] == player and board[y + 3][x + 3] == player):
        axe[2] = 1
        return axe

    if ((y - 2 >= 0 and y + 3 < size) and (x - 2 >= 0 and x + 3 < size)) and \
            (board[y - 2][x - 2] == 0 and board[y + 3][x + 3] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 1][x + 1] == player and board[y + 2][x + 2] == player):
        axe[2] = 1
        return axe

    if ((y - 3 >= 0 and y + 2 < size) and (x - 3 >= 0 and x + 2 < size)) and \
            (board[y - 3][x - 3] == 0 and board[y + 2][x + 2] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 2][x + 2] == player and board[y + 1][x + 1] == player):
        axe[2] = 1
        return axe

    if ((y - 4 >= 0 and y + 1 < size) and (x - 4 >= 0 and x + 1 < size)) and \
            (board[y - 4][x - 4] == 0 and board[y + 1][x + 1] == 0) and \
            (board[y - 1][x - 1] == player and board[y - 2][x - 2] == player and board[y - 3][x - 3] == player):
        axe[2] = 1
        return axe
    return axe


def dang_diagonal_right(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if ((y - 1 >= 0 and y + 4 < size) and (x - 4 >= 0 and x + 1 < size)) and \
            (board[y - 1][x + 1] == 0 and board[y + 4][x - 4] == 0) and \
            (board[y + 1][x - 1] == player and board[y + 2][x - 2] == player and board[y + 3][x - 3] == player):
        axe[2] = 1
        return axe

    if ((y - 2 >= 0 and y + 3 < size) and (x - 3 >= 0 and x + 2 < size)) and \
            (board[y - 2][x + 2] == 0 and board[y + 3][x - 3] == 0) and \
            (board[y - 1][x + 1] == player and board[y + 1][x + 1] == player and board[y + 2][x - 2] == player):
        axe[2] = 1
        return axe

    if ((y - 3 >= 0 and y + 2 < size) and (x - 2 >= 0 and x + 3 < size)) and \
            (board[y - 3][x + 3] == 0 and board[y + 2][x - 2] == 0) and \
            (board[y - 1][x + 1] == player and board[y - 2][x + 2] == player and board[y + 1][x - 1] == player):
        axe[2] = 1
        return axe

    if ((y - 4 >= 0 and y + 1 < size) and (x - 1 >= 0 and x + 4 < size)) and \
            (board[y - 4][x + 4] == 0 and board[y + 1][x - 1] == 0) and \
            (board[y - 1][x + 1] == player and board[y - 2][x + 2] == player and board[y - 3][x + 3] == player):
        axe[2] = 1
        return axe
    return axe


def dang_horizontal(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if (y - 1 >= 0 and y + 4 < size) and \
            (board[y - 1][x] == 0 and board[y + 4][x] == 0) and \
            (board[y + 1][x] == player and board[y + 2][x] == player and board[y + 3][x] == player):
        axe[2] = 1
        return axe
    if (y - 2 >= 0 and y + 3 < size) and \
            (board[y - 2][x] == 0 and board[y + 3][x] == 0) and \
            (board[y - 1][x] == player and board[y + 1][x] == player and board[y + 2][x] == player):
        axe[2] = 1
        return axe
    if (y - 3 >= 0 and y + 2 < size) and \
            (board[y - 3][x] == 0 and board[y + 2][x] == 0) and \
            (board[y - 1][x] == player and board[y - 2][x] == player and board[y + 1][x] == player):
        axe[2] = 1
        return axe
    if (y - 4 >= 0 and y + 1 < size) and \
            (board[y - 4][x] == 0 and board[y + 1][x] == 0) and \
            (board[y - 1][x] == player and board[y - 2][x] == player and board[y - 3][x] == player):
        axe[2] = 1
        return axe
    return axe


def dang_vertical(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if (x - 1 >= 0 and x + 4 < size) and \
            (board[y][x - 1] == 0 and board[y][x + 4] == 0) and \
            (board[y][x + 1] == player and board[y][x + 2] == player and board[y][x + 3] == player):
        axe[2] = 1
        return axe

    if (x - 2 >= 0 and x + 3 < size) and \
            (board[y][x - 2] == 0 and board[y][x + 3] == 0) and \
            (board[y][x - 1] == player and board[y][x + 1] == player and board[y][x + 2] == player):
        axe[2] = 1
        return axe

    if (x - 3 >= 0 and x + 2 < size) and \
            (board[y][x - 3] == 0 and board[y][x + 2] == 0) and \
            (board[y][x - 1] == player and board[y][x - 2] == player and board[y][x + 1] == player):
        axe[2] = 1
        return axe

    if (x - 4 >= 0 and x + 1 < size) and \
            (board[y][x - 4] == 0 and board[y][x + 1] == 0) and \
            (board[y][x - 1] == player and board[y][x - 2] == player and board[y][x - 3] == player):
        axe[2] = 1
        return axe
    return axe


def check_lose(board, axe, player):
    p = 1
    if player == 1:
        p = 0
    tab_players = [0, 0]
    get_nb_match_pawn.check_horizontal(board, 5, tab_players)
    get_nb_match_pawn.check_vertical(board, 5, tab_players)
    get_nb_match_pawn.check_diagonal_right(board, 5, tab_players)
    get_nb_match_pawn.check_diagonal_left(board, 5, tab_players)
    if tab_players[p] > 0:
        axe[2] = 1
    return axe


def alarm_manager(board, axe, player):
    lose = check_lose(board, axe, player)
    if lose[2] > 0:
        return lose
    if dang_vertical(board, axe, player)[2] == 1 or \
            dang_horizontal(board, axe, player)[2] == 1 or \
            dang_diagonal_right(board, axe, player)[2] == 1 or \
            dang_diagonal_left(board, axe, player)[2] == 1:
        axe[2] = 1
    return axe


def check_win_first(board, axe, player):
    p = 1
    if player == 1:
        p = 0
    tab_players = [0, 0]
    get_nb_match_pawn.check_diagonal_left(board, 5, tab_players)
    if tab_players[0] > 0:
        axe[2] = 1
        return axe

    tab_players = [0, 0]
    get_nb_match_pawn.check_diagonal_right(board, 5, tab_players)
    if tab_players[p] > 0:
        axe[2] = 1
        return axe

    tab_players = [0, 0]
    get_nb_match_pawn.check_vertical(board, 5, tab_players)
    if tab_players[p] > 0:
        axe[2] = 1
        return axe

    tab_players = [0, 0]
    get_nb_match_pawn.check_horizontal(board, 5, tab_players)
    if tab_players[p] > 0:
        axe[2] = 1
        return axe
    return axe


def is_win(board, player):
    axe = [0, 0, 0, 0]
    size = len(board[0])
    while axe[0] < size:
        axe[1] = 0
        while axe[1] < size:
            if board[axe[0]][axe[1]] == 0:
                board[axe[0]][axe[1]] = player
                axe = check_win_first(board, axe, player)
                board[axe[0]][axe[1]] = 0
                if axe[2] == 1:
                    return axe
            axe[1] += 1
        axe[0] += 1
    return axe


def check_alarm(board, player):
    axe = [0, 0, 0, 0]

    size = len(board[0])
    while axe[0] < size:
        axe[1] = 0
        while axe[1] < size:
            if board[axe[0]][axe[1]] == 0:
                board[axe[0]][axe[1]] = player
                axe = alarm_manager(board, axe, player)
                board[axe[0]][axe[1]] = 0
                if axe[2] == 1:
                    return axe
            axe[1] += 1
        axe[0] += 1
    return axe
