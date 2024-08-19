def solution(k, m, score):
    answer = 0
    score.sort()
    end = len(score)
    start = end - m
    while start > -1:
        # print(score[start:end])
        answer += score[start]*m
        start -= m

    # print(answer)
    return answer


if __name__ == "__main__":
    solution(3, 4, [1, 2, 3, 1, 2, 3, 1])
    solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])
