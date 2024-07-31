def solution(maps):
    answer = []
    y_max = len(maps)
    x_max = len(maps[0])
    visit = [[0 for _ in range(x_max)] for _ in range(y_max)]

    def BFS(start_point, maps, visit):
        to_blocks = [[-1,0],[0,1],[1,0],[0,-1]] # up, right, down, left
        start = [start_point]
        end = []
        days = int(maps[start_point[0]][start_point[1]])
        visit[start_point[0]][start_point[1]] = 1

        while len(start) != 0:
            for s in start:
                for to in to_blocks:
                    next_y = s[0] + to[0]
                    next_x = s[1] + to[1]
                    if 0 <= next_y and next_y < y_max and 0 <= next_x and next_x < x_max:
                        if maps[next_y][next_x] == 'X' or visit[next_y][next_x] == 1:
                            continue
                        days += int(maps[next_y][next_x])
                        visit[next_y][next_x] = 1
                        end.append([next_y, next_x])
            start = end
            end = []
        return days
    
    for y in range(y_max):
        for x in range(x_max):
            if maps[y][x] == "X" or visit[y][x] == 1:
                continue
            days = BFS([y,x], maps, visit)
            if days != -1:
                answer.append(days)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(["X591X","X1X5X","X231X", "1XXX1"])
    solution(["XXX","XXX","XXX"])
