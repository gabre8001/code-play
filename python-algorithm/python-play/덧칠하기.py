def solution(n, m, section):
    answer = 0
    start = 1

    wall = [1 for _ in range(n+1)]
    for s in section:
        wall[s] = 0
    
    while start <= n:
        if wall[start] == 0:
            for i in range(start, start+m):
                if i > n:
                    break
                wall[i] = 1
            start += m
            answer += 1
        else:
            start += 1
    # print(answer)
    return answer



if __name__ == "__main__":
    solution(8, 4, [2, 3, 6])
    solution(5, 4, [1, 3])
    solution(4, 1, [1, 2, 3, 4])
