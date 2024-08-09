def solution(k, d):
    answer = 0

    for x in range(0, d+1, k):
        point_num = (d**2 - (x)**2)**0.5//k
        # print("point_num", point_num)
        answer += (point_num + 1)

    # print("answer", answer)
    return answer



if __name__ == "__main__":
    solution(2, 4)
    solution(1, 5)
