def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries_sum = 0
    pickups_sum = 0
    cnt = 0

    for i in range(n-1, -1, -1):
        deliveries_sum += deliveries[i]
        pickups_sum += pickups[i]
        while deliveries_sum > cnt*cap or pickups_sum > cnt*cap:
            cnt+=1
            # print(i, cnt)
            # print(deliveries_sum, pickups_sum)
            answer +=  (i+1) * 2
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
    solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
    solution(2, 7, [3, 0, 2, 0, 1, 0, 2], [2, 2, 0, 1, 0, 2, 0])

    solution(2, 2, [1,10], [10,1])
    solution(2, 2, [1,4], [4,1])

    solution(4, 6, [0, 1, 0, 3, 1, 2], [0, 0, 3, 0, 4, 0])
