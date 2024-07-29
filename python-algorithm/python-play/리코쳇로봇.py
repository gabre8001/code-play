import sys

def solution(board):
    answer = -1
    x_len = len(board[0])
    y_len = len(board)
    grid = []
    visit = []
    point = []
    
    for y in range(y_len):
        temp_b = []
        temp_g = []
        for x in range(x_len):
            temp_b.append(board[y][x])
            temp_g.append(0)
            if board[y][x] == "R":
                point = [y, x]
        grid.append(temp_b)
        visit.append(temp_g)
    
    # Left, Up, Right, Down
    direction_list = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def go_from(y, x, direction, step):
        s_y = y
        s_x = x
        while (y >= 0 and y < y_len) and (x >= 0 and x < x_len) and (grid[y][x] != "D"):
            y += direction_list[direction][0]
            x += direction_list[direction][1]
            # print(y, x)
        y -= direction_list[direction][0]
        x -= direction_list[direction][1]
        if visit[y][x] == 0:
            visit[y][x] = 1
            return [y, x]
        else:
            return [s_y, s_x]
    start=[point]
    end = []
    visit[point[0]][point[1]] = 1
    step = 0
    while len(start) != 0:
        step += 1
        for s in start:
            for i in range(4):
                go_to = go_from(s[0], s[1], i, step)
                # print(go_to[0], go_to[1], s[0], s[1])
                if go_to[0] == s[0] and go_to[1] == s[1]:
                    continue
                if grid[go_to[0]][go_to[1]] == "G":
                    return step
                end.append(go_to)
        start = end
        end = []

    return answer


# This solution2 is wrong.
temp_answer = 0
def solution2(board):
    answer = -1
    global temp_answer
    temp_answer = sys.maxsize
    direction_list = [0, 1, 2, 3] # Left, Up, Right, Down
    x_len = len(board[0])
    y_len = len(board)
    grid = []
    go_to = []
    point = []
    for y in range(y_len):
        temp_b = []
        temp_g = []
        for x in range(x_len):
            temp_b.append(board[y][x])
            temp_g.append([])
            if board[y][x] == "R":
                point = [y, x]
        grid.append(temp_b)
        go_to.append(temp_g)

    # print(board)
    # print(grid)
    # print(go_to)
    # print(point)

    def dfs(step, y, x, direction):
        # if step == 100:
        #     return
        global temp_answer
        if step > temp_answer:
            return
        # print(step, grid[y][x], y, x, direction)
        go_to[y][x].append(direction)
        
        if board[y][x] == "G":
            if temp_answer > step:
                temp_answer = step
            return step
        step += 1
        # go up - not from down
        if 1 not in go_to[y][x] and y != 0:
            column = [row[x] for row in grid[:y]]
            indices = [index for index, value in enumerate(column) if value == "D"]
            # print("up", y, x, column)
            go_to[y][x].append(1)
            if len(indices) == 0:
                dfs(step, 0, x, 1)
            else:
                dfs(step, max(indices)+1, x, 1)
            go_to[y][x].remove(1)
        
        # go down - not from up
        if 3 not in go_to[y][x] and y is not y_len - 1:
            column = [row[x] for row in grid[y:]]
            indices = [index for index, value in enumerate(column) if value == "D"]
            # print("down", y, x, column)
            go_to[y][x].append(3)
            if len(indices) == 0:
                dfs(step, y_len - 1, x, 3)
            else:
                dfs(step, min(indices)-1, x, 3)
            go_to[y][x].remove(3)

        # go left - not from right
        if 0 not in go_to[y][x] and x != 0:
            row = grid[y][:x]
            indices = [index for index, value in enumerate(row) if value == "D"]
            # print("left", y, x, row)
            go_to[y][x].append(0)
            if len(indices) == 0:
                dfs(step, y, 0, 0)
            else:
                dfs(step, y, max(indices)+1, 0)
            go_to[y][x].remove(0)
        
        # go right - not from left
        if 2 not in go_to[y][x] and x is not x_len - 1:
            row = grid[y][x:]
            indices = [index for index, value in enumerate(row) if value == "D"]
            # print("right", y, x, row)
            go_to[y][x].append(2)
            if len(indices) == 0:
                dfs(step, y, x_len - 1, 2)
            else:
                dfs(step, y, min(indices)-1, 2)
            go_to[y][x].remove(2)
                
        return -1

    dfs(0, point[0], point[1], -1)
    if temp_answer != sys.maxsize:
        answer = temp_answer
    return answer


if __name__ == "__main__":
    answer = solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
    print(answer)
    answer = solution([".D.R", "....", ".G..", "...D"])
    print(answer)
