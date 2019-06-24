def solveSudoku(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # create a potential list of elements
    for row_index in range(9):
        for col_index in range(9):
            try:
                v_int = int(board[row_index][col_index])
            except ValueError:
                board[row_index][col_index] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    not_done = True
    i=0
    while not_done:
        if i == 10:
            break
        # check row
        for row_index in range(9):
            for col_index in range(9):
                if type(board[row_index][col_index]) == set:
                    tmp_set = board[row_index][col_index].copy()
                    orig_len = len(tmp_set)
                    same_indexes = [col_index]
                    for o_col_index in range(9):
                        if o_col_index == col_index:
                            continue
                        if type(board[row_index][o_col_index]) != set:
                            try:
                                v_int = int(board[row_index][o_col_index])
                            except (ValueError, TypeError):
                                continue
                            try:
                                board[row_index][col_index].remove(v_int)
                            except (KeyError, TypeError):
                                pass
                            try:
                                tmp_set.remove(v_int)
                            except (KeyError, TypeError):
                                continue
                        else:
                            if len(board[row_index][o_col_index]) <= orig_len and \
                                    len(board[row_index][col_index] & board[row_index][o_col_index]) == orig_len:
                                same_indexes.append(o_col_index)
                                #if len(same_indexes) == orig_len:
                                #    print("!")
                            #if len(board[row_index][col_index]) == 2 and len(board[row_index][o_col_index]) == 2 and\
                            #        len(board[row_index][col_index] & board[row_index][o_col_index]) == 2:
                            #    print(board[row_index][col_index])
                            #    print(board[row_index][o_col_index])
                            #    print("-1 \n")
                            #    # if the sets are identical, remove the values from other cols

                            tmp_set = tmp_set - board[row_index][o_col_index]

                    if len(same_indexes) == orig_len and orig_len >= 2:
                        print(same_indexes, orig_len,board[row_index][col_index])
                        for n_col_index in range(9):
                            if n_col_index not in same_indexes and\
                                    type(board[row_index][n_col_index]) == set:
                                board[row_index][n_col_index] = \
                                    board[row_index][n_col_index] - board[row_index][col_index]

                    if len(board[row_index][col_index]) == 1:
                        board[row_index][col_index] = str(board[row_index][col_index].pop())
                    elif len(tmp_set) == 1 and len(board[row_index][col_index] & tmp_set) == 1:
                        print("-1", row_index, col_index, tmp_set)
                        board[row_index][col_index] = str(tmp_set.pop())
        print("On iteration {}".format(i))
        for b in board:
            print(b)
        print("\n")
        # check column
        for col_index in range(9):
            for row_index in range(9):
                if type(board[row_index][col_index]) == set:
                    tmp_set = board[row_index][col_index].copy()
                    orig_len = len(tmp_set)
                    same_indexes = [row_index]
                    for o_row_index in range(9):
                        if o_row_index == row_index:
                            continue
                        if type(board[o_row_index][col_index]) != set:
                            try:
                                v_int = int(board[o_row_index][col_index])
                            except (ValueError, TypeError):
                                continue
                            try:
                                board[row_index][col_index].remove(v_int)
                            except (KeyError, TypeError):
                                pass
                            try:
                                tmp_set.remove(v_int)
                            except (KeyError, TypeError):
                                continue
                        else:
                            if len(board[o_row_index][col_index]) <= orig_len and \
                                    len(board[row_index][col_index] & board[o_row_index][col_index]) == orig_len:
                                same_indexes.append(o_row_index)

                            #if len(board[row_index][col_index]) == 2 and len(board[o_row_index][col_index]) == 2 and \
                            #        len(board[row_index][col_index] & board[o_row_index][col_index]) == 2:
                            #    print(board[row_index][col_index])
                            #    print(board[o_row_index][col_index])
                            #    print("-2 \n")
                            #    # if the sets are identical, remove the values from other cols
                            #    for n_row_index in range(9):
                            #        if n_row_index not in (row_index, o_row_index) and\
                            #                type(board[n_row_index][col_index]) == set:
                            #            board[n_row_index][col_index] = \
                            #                board[n_row_index][col_index] - board[row_index][col_index]
                            tmp_set = tmp_set - board[o_row_index][col_index]

                    if len(same_indexes) == orig_len and orig_len >= 2:
                        print(same_indexes, orig_len, board[row_index][col_index])
                        for n_row_index in range(9):
                            if n_row_index not in same_indexes and\
                                    type(board[n_row_index][col_index]) == set:
                                board[n_row_index][col_index] = \
                                    board[n_row_index][col_index] - board[row_index][col_index]

                    if len(board[row_index][col_index]) == 1:
                        board[row_index][col_index] = str(board[row_index][col_index].pop())
                    elif len(tmp_set) == 1 and len(board[row_index][col_index] & tmp_set) == 1:
                        print("-2", row_index, col_index, tmp_set)
                        board[row_index][col_index] = str(tmp_set.pop())
        print("On iteration {}".format(i))
        for b in board:
            print(b)
        print("\n")
        # check blocks
        for block_row_idx in range(3):
            for block_col_idx in range(3):
                # iterate through block
                for row_index in range(block_row_idx * 3,(block_row_idx + 1) * 3):
                    for col_index in range(block_col_idx * 3, (block_col_idx + 1) * 3):
                        if type(board[row_index][col_index]) == set:
                            tmp_set = board[row_index][col_index].copy()
                            orig_len = len(tmp_set)
                            same_indexes = [(row_index, col_index)]
                            # iterate through block for each spot with a set
                            for o_row_index in range(block_row_idx * 3, (block_row_idx + 1) * 3):
                                for o_col_index in range(block_col_idx * 3, (block_col_idx + 1) * 3):
                                    if o_col_index == col_index and o_row_index == row_index:
                                        continue
                                    if type(board[o_row_index][o_col_index]) != set:
                                        v_int = int(board[o_row_index][o_col_index])
                                        try:
                                            board[row_index][col_index].remove(v_int)
                                        except (KeyError, TypeError):
                                            pass
                                        try:
                                            tmp_set.remove(v_int)
                                        except (KeyError, TypeError):
                                            continue
                                    else:

                                        if len(board[o_row_index][o_col_index]) <= orig_len and \
                                                len(board[row_index][col_index] & board[o_row_index][o_col_index]) == orig_len:
                                            #same_row_indexes.append(o_row_index)
                                            #same_col_indexes.append(o_col_index)
                                            same_indexes.append((o_row_index, o_col_index))
                                        #if len(board[row_index][col_index]) == 2 and len(board[o_row_index][o_col_index]) == 2 and \
                                        #        len(board[row_index][col_index] & board[o_row_index][o_col_index]) == 2:
                                        #    print(row_index, col_index, board[row_index][col_index])
                                        #    print(board[o_row_index][o_col_index])
                                        #    print("-3 \n")
                                        #    # if the sets are identical, remove the values from other cols
                                        #    print(block_row_idx * 3, (block_row_idx + 1) * 3)
                                        #    print(block_col_idx * 3, (block_col_idx + 1) * 3)
                                        #    for n_row_index in range(block_row_idx * 3, (block_row_idx + 1) * 3):
                                        #        for n_col_index in range(block_col_idx * 3, (block_col_idx + 1) * 3):
                                        #            if n_row_index not in (row_index, o_row_index) and \
                                        #                    n_col_index not in (col_index, o_col_index) and\
                                        #                    type(board[n_row_index][n_col_index]) == set:
                                        #                board[n_row_index][n_col_index] = \
                                        #                    board[n_row_index][n_col_index] - board[row_index][col_index]

                                        tmp_set = tmp_set - board[o_row_index][o_col_index]

                            if len(same_indexes) == orig_len and orig_len >= 2:
                                print(same_indexes, orig_len, board[row_index][col_index])
                                for n_row_index in range(block_row_idx * 3, (block_row_idx + 1) * 3):
                                    for n_col_index in range(block_col_idx * 3, (block_col_idx + 1) * 3):
                                        skip = False
                                        for idx in range(len(same_indexes)):
                                            if n_row_index == same_indexes[idx][0] and n_col_index == same_indexes[idx][1]:
                                                print(n_row_index, n_col_index)
                                                skip = True
                                        if type(board[n_row_index][n_col_index]) == set and not skip:
                                            print(n_row_index, n_col_index)
                                            board[n_row_index][n_col_index] = \
                                                board[n_row_index][n_col_index] - board[row_index][col_index]
                            if len(board[row_index][col_index]) == 1:
                                board[row_index][col_index] = str(board[row_index][col_index].pop())
                            elif len(tmp_set) == 1 and len(board[row_index][col_index] & tmp_set) == 1:
                                print("-3", row_index, col_index, tmp_set)
                                board[row_index][col_index] = str(tmp_set.pop())

        # check if complete
        done = True
        for row_index in range(9):
            for col_index in range(9):
                if type(board[o_row_index][col_index]) == set:
                    done = False
                    break
        if done:
            not_done = False
        else:
            print("On iteration {}".format(i))
            for b in board:
                print(b)
            print("\n")
            i+=1


if __name__ == '__main__':
    #board = [
    #    ["5","3",".",".","7",".",".",".","."],
    #    ["6",".",".","1","9","5",".",".","."],
    #    [".","9","8",".",".",".",".","6","."],
    #    ["8",".",".",".","6",".",".",".","3"],
    #    ["4",".",".","8",".","3",".",".","1"],
    #    ["7",".",".",".","2",".",".",".","6"],
    #    [".","6",".",".",".",".","2","8","."],
    #    [".",".",".","4","1","9",".",".","5"],
    #    [".",".",".",".","8",".",".","7","9"]
    #]
    #solveSudoku(board)
    #for b in board:
    #    print(b)


    board = [
        [".",".","9","7","4","8",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        [".","2",".","1",".","9",".",".","."],
        [".",".","7",".",".",".","2","4","."],
        [".","6","4",".","1",".","5","9","."],
        [".","9","8",".",".",".","3",".","."],
        [".",".",".","8",".","3",".","2","."],
        [".",".",".",".",".",".",".",".","6"],
        [".",".",".","2","7","5","9",".","."]
    ]
    solveSudoku(board)
    for b in board:
        print(b)

