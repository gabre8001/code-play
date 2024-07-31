def solution(maps):
    answer = 0
    to_blocks = [[-1,0],[0,1],[1,0],[0,-1]] # up, right, down, left
    y_max = len(maps)
    x_max = len(maps[0])
    start_point = []
    lever_point = []
    exit_point = []
    visit = [] 
    for y in range(y_max):
        temp = []
        for x in range(x_max):
            temp.append(0)
            if maps[y][x] == "S":
                start_point = [y,x]
            if maps[y][x] == "L":
                lever_point = [y,x]
            if maps[y][x] == "E":
                exit_point = [y,x]
        visit.append(temp)
    

    def BFS(start_point, end_point, maps, visit):
        start = [start_point]
        end = []
        visit[start_point[0]][start_point[1]] = 1
        step = 0
        while len(start) != 0:
            step += 1
            for s in start:
                for to in to_blocks:
                    next_y = s[0] + to[0]
                    next_x = s[1] + to[1]
                    
                    if 0 <= next_y and next_y < y_max and 0 <= next_x and next_x < x_max:
                        if maps[next_y][next_x] == "X" or visit[next_y][next_x] == 1:
                            continue
                        visit[next_y][next_x] = 1
                        end.append([next_y, next_x])
                        if end_point[0] == next_y and end_point[1] == next_x:
                            return step
            if len(end) == 0:
                return -1
            start = end
            end = []
    
    to_lever = BFS(start_point, lever_point, maps, visit)
    if to_lever == -1:
        return -1
    visit = [[0 for _ in range(x_max)] for _ in range(y_max)]
    to_exit = BFS(lever_point, exit_point, maps, visit)
    if to_exit == -1:
        return -1
    # print(to_lever, to_exit)
    answer = to_lever + to_exit
    return answer


if __name__ == "__main__":
    solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])
    solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"])
