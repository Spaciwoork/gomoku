def check_diagonal_left(board, victories, tab_players):
    x = 0
    count_1 = 0
    count_2 = 0
    max1 = 0
    max2 = 0
    size = len(board[0])
    while x < size:
        y = 0
        x1 = x
        while y < size and x1 < size:
            if board[y][x1] == 1:
                count_1 += 1
                count_2 = 0
                if count_1 > max1:
                    max1 = count_1
                if count_1 == victories:
                    tab_players[0] += 1
            elif board[y][x1] == 2:
                count_2 += 1
                count_1 = 0
                if count_2 > max2:
                    max2 = count_2
                if count_2 == victories:
                    tab_players[1] += 1
            else:
                count_2 = 0
                count_1 = 0
            x1 += 1
            y += 1
        x += 1

    y = 1
    count_1 = 0
    count_2 = 0
    while y < size:
        y1 = y
        x = 0
        while y1 < size and x < size:
            if board[y1][x] == 1:
                count_1 += 1
                count_2 = 0
                if count_1 > max1:
                    max1 = count_1
                if count_1 == victories:
                    tab_players[0] += 1
            elif board[y1][x] == 2:
                count_2 += 1
                count_1 = 0
                if count_2 > max2:
                    max2 = count_2
                if count_2 == victories:
                    tab_players[1] += 1
            else:
                count_2 = 0
                count_1 = 0
            x += 1
            y1 += 1
        y += 1
    return [max1, max2]


def check_diagonal_right(board, victories, tab_players):
    x = 0
    count_1 = 0
    count_2 = 0
    max1 = 0
    max2 = 0
    size = len(board[0])
    while x < size:
        y = 0
        x1 = x
        while y < size and x1 >= 0:
            if board[y][x1] == 1:
                count_1 += 1
                count_2 = 0
                if count_1 > max1:
                    max1 = count_1
                if count_1 == victories:
                    tab_players[0] += 1
            elif board[y][x1] == 2:
                count_2 += 1
                count_1 = 0
                if count_2 > max2:
                    max2 = count_2
                if count_2 == victories:
                    tab_players[1] += 1
            else:
                count_2 = 0
                count_1 = 0
            x1 -= 1
            y += 1
        x += 1

    y = 1
    count_1 = 0
    count_2 = 0
    while y < size:
        y1 = y
        x = size - 1
        while y1 < size and x >= 0:
            if board[y1][x] == 1:
                count_1 += 1
                count_2 = 0
                if count_1 > max1:
                    max1 = count_1
                if count_1 == victories:
                    tab_players[0] += 1
            elif board[y1][x] == 2:
                count_2 += 1
                count_1 = 0
                if count_2 > max2:
                    max2 = count_2
                if count_2 == victories:
                    tab_players[1] += 1
            else:
                count_2 = 0
                count_1 = 0
            x -= 1
            y1 += 1
        y += 1
    return [max1, max2]


def check_horizontal(board, victories, tab_players):
    x = 0
    max1 = 0
    max2 = 0
    while x < len(board[0]):
        count1 = 0
        count2 = 0
        y = 0
        while y < len(board[0]):
            if board[y][x] == 1:
                count1 += 1
                count2 = 0
                if count1 > max1:
                    max1 = count1
                if count1 == victories:
                    tab_players[0] += 1
            elif board[y][x] == 2:
                count2 += 1
                count1 = 0
                if count2 > max2:
                    max2 = count2
                if count2 == victories:
                    tab_players[1] += 1
            else:
                count1 = 0
                count2 = 0
            y += 1
        x += 1
    return [max1, max2]


def check_vertical(board, victories, tab_players):
    max1 = 0
    max2 = 0
    y = 0
    while y < len(board[0]):
        count1 = 0
        count2 = 0
        x = 0
        while x < len(board[0]):
            if board[y][x] == 1:
                count1 += 1
                count2 = 0
                if count1 > max1:
                    max1 = count1
                if count1 == victories:
                    tab_players[0] += 1
            elif board[y][x] == 2:
                count2 += 1
                count1 = 0
                if count2 > max2:
                    max2 = count2
                if count2 == victories:
                    tab_players[1] += 1
            else:
                count1 = 0
                count2 = 0
            x += 1
        y += 1
    return [max1, max2]


def check_series(board, victories):
    tab_players = [0, 0, 0, 0]
    res = [0, 0]
    res1 = check_vertical(board, victories, tab_players)
    if res1[0] > res[0]:
        res[0] = res1[0]
    if res1[1] > res[1]:
        res[1] = res1[1]
    res2 = check_horizontal(board, victories, tab_players)
    if res2[0] > res[0]:
        res[0] = res2[0]
    if res2[1] > res[1]:
        res[1] = res2[1]
    res3 = check_diagonal_right(board, victories, tab_players)
    if res3[0] > res[0]:
        res[0] = res3[0]
    if res3[1] > res[1]:
        res[1] = res3[1]
    res4 = check_diagonal_left(board, victories, tab_players)
    if res4[0] > res[0]:
        res[0] = res4[0]
    if res4[1] > res[1]:
        res[1] = res4[1]
    tab_players[2] = res[0]
    tab_players[3] = res[1]
    return tab_players
