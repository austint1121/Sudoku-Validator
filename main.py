def valid_solution(board):
    """
    The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row,
    and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
    """
    for x, lists in enumerate(board):  # Rows
        convert = set(lists)
        if 0 in convert or len(convert) < 9:
            return False
    columns = set()
    for x in range(0, 9):  # Columns
        for y in range(0, 9):
            target = board[y]
            columns.add(target[x])
        if 0 in columns or len(columns) < 9:
            return False
        columns.clear()
    squares1 = set()
    squares2 = set()
    squares3 = set()
    for x in range(0, 9):  # Squares
        for y in range(0, 3):
            squares1.add(board[x][y])
            squares2.add(board[x][y+3])
            squares3.add(board[x][y+6])
        if (x + 1) % 3 == 0:
            if 0 in squares1 or len(squares1) < 9:
                return False
            if 0 in squares2 or len(squares2) < 9:
                return False
            if 0 in squares3 or len(squares3) < 9:
                return False
            squares1.clear(), squares2.clear(), squares3.clear()
    return True
