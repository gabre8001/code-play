import heapq
def solution(k, score):
    answer = []
    q = []

    for s in score:
        if len(q) < k:
            heapq.heappush(q, s)
        else:
            heapq.heappush(q, s)
            heapq.heappop(q)
        answer.append(q[0])
    # print(answer)
    return answer



if __name__ == "__main__":
    solution(3, [10, 100, 20, 150, 1, 100, 200])
    solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
