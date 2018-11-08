from algo import peril


def attack_diagonal_left1(board, axe):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 1 >= 0 and x + 3 < size)) and \
            (board[y - 1][x - 1] == 0 and board[y + 1][x + 1] == 0 and board[y + 2][x + 2] == 0 and
             board[y + 3][x + 3] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_diagonal_left2(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 1 >= 0 and x + 3 < size)) and \
            (board[y - 1][x - 1] == 0 and board[y + 3][x + 3] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 2][x + 2] == 0):
        axe[2] = 1
        return axe

    if ((y - 2 >= 0 and y + 2 < size) and (x - 2 >= 0 and x + 2 < size)) and \
            (board[y - 2][x - 2] == 0 and board[y + 2][x + 2] == 0) and \
            (board[y - 1][x - 1] == player and board[y + 1][x + 1] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_diagonal_left3(board, axe, player):
    y = axe[0]
    x = axe[1]

    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 1 >= 0 and x + 3 < size)) and \
            (board[y - 1][x - 1] == 0 and board[y + 3][x + 3] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 2][x + 2] == player):
        axe[2] = 1
        return axe
    if ((y - 2 >= 0 and y + 2 < size) and (x - 2 >= 0 and x + 2 < size)) and \
            (board[y - 2][x - 2] == 0 and board[y + 2][x + 2] == 0) and \
            (board[y - 1][x - 1] == player and board[y + 1][x + 1] == player):
        axe[2] = 1
        return axe
    if ((y - 3 >= 0 and y + 1 < size) and (x - 3 >= 0 and x + 1 < size)) and \
            (board[y - 3][x - 3] == 0 and board[y + 1][x + 1] == 0) and \
            (board[y + 1][x + 1] == player and board[y + 2][x + 2] == player):
        axe[2] = 1
        return axe
    return axe


def attack_diagonal_right1(board, axe):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 3 >= 0 and x + 1 < size)) and \
            (board[y - 1][x + 1] == 0 and board[y + 1][x - 1] == 0 and
             board[y + 2][x - 2] == 0 and board[y + 3][x - 3] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_diagonal_right2(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 3 >= 0 and x + 1 < size)) and \
            (board[y - 1][x + 1] == 0 and board[y + 3][x - 3] == 0) and \
            (board[y + 1][x - 1] == player and board[y + 2][x - 2] == 0):
        axe[2] = 1
        return axe

    if ((y - 2 >= 0 and y + 2 < size) and (x - 2 >= 0 and x + 2 < size)) and \
            (board[y - 2][x + 2] == 0 and board[y + 2][x - 2] == 0) and \
            (board[y - 1][x + 1] == player):
        axe[2] = 1
        return axe
    return axe


def attack_diagonal_right3(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if ((y - 1 >= 0 and y + 3 < size) and (x - 3 >= 0 and x + 1 < size)) and \
            (board[y - 1][x + 1] == 0 and board[y + 3][x - 3] == 0) and \
            (board[y + 1][x - 1] == player and board[y + 2][x - 2] == player):
        axe[2] = 1
        return axe
    if ((y - 2 >= 0 and y + 2 < size) and (x - 2 >= 0 and x + 2 < size)) and \
            (board[y - 2][x + 2] == 0 and board[y + 2][x - 2] == 0) and \
            (board[y - 1][x + 1] == player and board[y + 1][x + 1] == player):
        axe[2] = 1
        return axe
    if ((y - 3 >= 0 and y + 1 < size) and (x - 1 >= 0 and x + 3 < size)) and \
            (board[y - 3][x + 3] == 0 and board[y + 1][x - 1] == 0) and \
            (board[y - 1][x + 1] == player and board[y - 2][x + 2] == player):
        axe[2] = 1
        return axe
    return axe


def attack_horizontal1(board, axe):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (y - 1 >= 0 and y + 3 < size) and \
            (board[y - 1][x] == 0 and board[y + 3][x] == 0 and board[y + 1][x] == 0 and board[y + 2][x] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_horizontal2(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (y - 1 >= 0 and y + 3 < size) and \
            (board[y - 1][x] == 0 and board[y + 3][x] == 0) and \
            (board[y + 1][x] == player and board[y + 2][x] == 0):
        axe[2] = 1
        return axe
    if (y - 2 >= 0 and y + 2 < size) and \
            (board[y - 2][x] == 0 and board[y + 2][x] == 0) and \
            (board[y - 1][x] == player and board[y + 1][x] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_horizontal3(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (y - 1 >= 0 and y + 3 < size) and \
            (board[y - 1][x] == 0 and board[y + 3][x] == 0) and \
            (board[y + 1][x] == player and board[y + 2][x] == player):
        axe[2] = 1
        return axe
    if (y - 2 >= 0 and y + 2 < size) and \
            (board[y - 2][x] == 0 and board[y + 2][x] == 0) and \
            (board[y - 1][x] == player and board[y + 1][x] == player):
        axe[2] = 1
        return axe
    if (y - 3 >= 0 and y + 1 < size) and \
            (board[y - 3][x] == 0 and board[y + 1][x] == 0) and \
            (board[y - 1][x] == player and board[y - 2][x] == player):
        axe[2] = 1
        return axe
    return axe


def attack_vertical1(board, axe):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (x - 1 >= 0 and x + 3 < size) and \
            (board[y][x - 1] == 0 and board[y][x + 3] == 0 and board[y][x + 1] == 0 and board[y][x + 2] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_vertical2(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (x - 1 >= 0 and x + 3 < size) and \
            (board[y][x - 1] == 0 and board[y][x + 3] == 0) and \
            (board[y][x + 1] == player and board[y][x + 2] == 0):
        axe[2] = 1
        return axe
    if (x - 2 >= 0 and x + 2 < size) and \
            (board[y][x - 2] == 0 and board[y][x + 2] == 0) and \
            (board[y][x - 1] == player and board[y][x + 1] == 0):
        axe[2] = 1
        return axe
    return axe


def attack_vertical3(board, axe, player):
    y = axe[0]
    x = axe[1]
    size = len(board[0])
    if (x - 1 >= 0 and x + 3 < size) and \
            (board[y][x - 1] == 0 and board[y][x + 3] == 0) and \
            (board[y][x + 1] == player and board[y][x + 2] == player):
        axe[2] = 1
        return axe
    if (x - 2 >= 0 and x + 2 < size) and \
            (board[y][x - 2] == 0 and board[y][x + 2] == 0) and \
            (board[y][x - 1] == player and board[y][x + 1] == player):
        axe[2] = 1
        return axe
    if (x - 3 >= 0 and x + 1 < size) and \
            (board[y][x - 3] == 0 and board[y][x + 1] == 0) and \
            (board[y][x - 1] == player and board[y][x - 2] == player):
        axe[2] = 1
        return axe
    return axe


def attack_manager(board, axe, player, var):
    if var == 1:
        if attack_vertical1(board, axe)[2] == 1 or \
                attack_horizontal1(board, axe)[2] == 1 or \
                attack_diagonal_right1(board, axe)[2] == 1 or \
                attack_diagonal_left1(board, axe)[2] == 1:
            axe[2] = 1
    elif var == 2:
        if attack_vertical2(board, axe, player)[2] == 1 or \
                attack_horizontal2(board, axe, player)[2] == 1 or \
                attack_diagonal_right2(board, axe, player)[2] == 1 or \
                attack_diagonal_left2(board, axe, player)[2] == 1:
            axe[2] = 1
    elif var == 3:
        if attack_vertical3(board, axe, player)[2] == 1 or \
                attack_horizontal3(board, axe, player)[2] == 1 or \
                attack_diagonal_right3(board, axe, player)[2] == 1 or \
                attack_diagonal_left3(board, axe, player)[2] == 1:
            axe[2] = 1
    return axe


def get_attack(board, player):
    axe = [0, 0, 0, 0]
    size = len(board[0])
    i = 3
    while i > 0:
        axe[0] = 0
        while axe[0] < size:
            axe[1] = 0
            while axe[1] < size:
                if board[axe[0]][axe[1]] == 0:
                    board[axe[0]][axe[1]] = player
                    if peril.alarm_manager(board, axe, 1)[2] > 0:
                        return axe
                    axe = attack_manager(board, axe, player, i)
                    board[axe[0]][axe[1]] = 0
                    if axe[2] == 1:
                        return axe
                axe[1] += 1
            axe[0] += 1
        i -= 1
    return axe
