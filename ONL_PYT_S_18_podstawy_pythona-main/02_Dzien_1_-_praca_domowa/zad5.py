def chessboard(n=8):
    board = ''
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board += '#'
            else:
                board += ' '
        board += '\n'
    return board

c = chessboard()
print(c)