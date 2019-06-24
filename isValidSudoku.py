

def isValidSudoku(board) -> bool:
    # test board is correct size
    if len(board) != 9:
        return False
    if not all([len(l) == 9 for l in board]):
        return False
    # test rows
    for rows in board:
        # set will only add new elements, copies will not be added
        # if the # of numbers = length of the set, then there are no duplicates
        count_values = 0
        set_values = set()
        for value in rows:
            try:
                v_int = int(value)
            except ValueError:
                continue
            if 1 <= v_int <= 9:
                set_values.add(v_int)
                count_values += 1
        if len(set_values) < count_values:
            return False
    # test columns
    for col_index in range(9):
        # set will only add new elements, copies will not be added
        # if the # of numbers = length of the set, then there are no duplicates
        count_values = 0
        set_values = set()
        for row_index in range(9):
            try:
                v_int = int(board[row_index][col_index])
            except ValueError:
                continue
            if 1 <= v_int <= 9:
                set_values.add(v_int)
                count_values += 1
        if len(set_values) < count_values:
            return False

    # test blocks
    for block_row_idx in range(3):
        for block_col_idx in range(3):
            count_values = 0
            set_values = set()
            for row in board[block_row_idx*3:(block_row_idx+1)*3]:
                for value in row[block_col_idx * 3: (block_col_idx + 1) * 3]:
                    try:
                        v_int = int(value)
                    except ValueError:
                        continue
                    if 1 <= v_int <= 9:
                        set_values.add(v_int)
                        count_values += 1
            if len(set_values) < count_values:
                return False

    return True


if __name__ == '__main__':
    print(isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))

    print(isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))