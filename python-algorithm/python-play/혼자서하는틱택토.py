def solution(board):
    b_len = len(board)

    def count_symbol():
        count_o = 0
        count_x = 0
        for i in range(b_len):
            for j in range(b_len):
                if board[i][j] == "O":
                    count_o += 1
                if board[i][j] == "X":
                    count_x += 1
        return count_o, count_x
    
    def win_count():
        count_o = 0
        count_x = 0
        win_o_count = 0
        win_x_count = 0
        for i in range(b_len):
            count_o = 0
            count_x = 0
            for j in range(b_len):
                if board[i][j] == "O":
                    count_o += 1
                if board[i][j] == "X":
                    count_x += 1
            if count_o == 3:
                win_o_count += 1
            if count_x == 3:
                win_x_count += 1
        
        for j in range(b_len):
            count_o = 0
            count_x = 0
            for i in range(b_len):
                if board[i][j] == "O":
                    count_o += 1
                if board[i][j] == "X":
                    count_x += 1
            if count_o == 3:
                win_o_count += 1
            if count_x == 3:
                win_x_count += 1
        
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            win_o_count += 1
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            win_x_count += 1
        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            win_o_count += 1
        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            win_x_count += 1

        return win_o_count, win_x_count
    
    count_o, count_x = count_symbol()
    win_o, win_x = win_count()
    # print(count_o, count_x, win_o, win_x)
    if count_o != count_x and count_o - count_x != 1:
        return 0
    if win_o >= 1 and win_x >= 1:
        return 0
    if win_o >= 1 and count_o - count_x != 1:
        return 0
    if win_x >= 1 and count_o - count_x != 0:
        return 0
    return 1



if __name__ == "__main__":
    print(solution(["O.X", ".O.", "..X"]))
    print(solution(["OOO", "...", "XXX"]))
    print(solution(["...", ".X.", "..."]))
    print(solution(["...", "...", "..."]))
    print(solution(["OOO", "XOX", "XXO"]))
    print(solution(["XO.", "OXO", "XOX"]))
    print(solution(["OO.", "XXX", "OO."]))
    print(solution(["OOO", "OXX", "OXX"]))
