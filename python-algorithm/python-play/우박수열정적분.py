def solution(k, ranges):
    answer = []
    l = []
    num = k
    l.append(k)

    while num != 1:
        if num % 2 == 1:
            num *= 3
            num += 1
        else:
            num = num//2
        l.append(num)
    # print(l)
    l_int = []
    for i in range(len(l) - 1):
        l_int.append((l[i] + l[i+1])/2)
    # print(l_int)
    for r in ranges:
        start = r[0]
        end = len(l)+r[1]-1
        if start == end:
            answer.append(0.0)
        elif start > end:
            answer.append(-1.0)
        else:
            answer.append(sum(l_int[start:end]))
    # print(answer)
    return answer


if __name__ =="__main__":
    solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])
    solution(3, [[0,0], [1,-2], [3,-3]])
