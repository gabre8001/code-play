def solution(ingredient):
    answer = 0
    q = []

    for ing in ingredient:
        q.append(ing)
        if len(q) >= 4:
            if q[-1] == 1 and q[-2] == 3 and q[-3] == 2 and q[-4] == 1:
                q.pop()
                q.pop()
                q.pop()
                q.pop()
                answer += 1
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
    solution([1, 3, 2, 1, 2, 1, 3, 1, 2])
