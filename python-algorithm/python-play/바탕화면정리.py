def solution(wallpaper):
    answer = []
    x_max = len(wallpaper)
    y_max = len(wallpaper[0])
    lux, luy = 100, 100
    rdx, rdy = 0, 0

    for x in range(x_max):
        for y in range(y_max):
            if wallpaper[x][y] == "#":
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x)
                rdy = max(rdy, y)

    answer = [lux, luy, rdx+1, rdy+1]
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([".#...", "..#..", "...#."])
    solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
    solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
    solution(["..", "#."])
