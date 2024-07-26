def solution(park, routes):
    answer = []
    point = []
    mat = [[x for x in p] for p in park]
    y_max = len(park)
    x_max = len(park[0])
    for y in range(y_max):
        for x in range(x_max):
            if park[y][x] == "S":
                point = [y,x]
                break
    # print(y_max, x_max)
    # print(mat)
    # print([row[1] for row in mat])


    for r in routes:
        r_arr = r.split(" ")
        direction = r_arr[0]
        step = int(r_arr[1])
        if direction == "N":
            if 0 <= (point[0] - step):
                column = [row[point[1]] for row in mat]
                # print("N", column[point[0] - step: point[0]+1])
                if "X" not in column[point[0] - step: point[0]+1]:
                    point[0] -= step
        elif direction == "S":
            if (point[0] + step) < y_max:
                column = [row[point[1]] for row in mat]
                # print("S", column[point[0]: point[0]+step+1])
                if "X" not in column[point[0]: point[0]+step+1]:
                    point[0] += step
        elif direction == "W":
            if 0 <= (point[1] - step):
                row = mat[point[0]]
                # print("W", row[point[1] - step: point[1]+1])
                if "X" not in row[point[1] - step: point[1]+1]:
                    point[1] -= step
        elif direction == "E":
            if (point[1] + step) < x_max:
                row = mat[point[0]]
                # print("E", row[point[1]: point[1]+step+1])
                if "X" not in row[point[1]: point[1]+step+1]:
                    point[1] += step
    # print(point)
    answer = point
    return answer


if __name__ == "__main__":
    solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])
    solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"])
    solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])
