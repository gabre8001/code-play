def solution(number, limit, power):
    answer = 0
    p_list = []
    count = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i**(1/2)) + 1):
            if (i % j == 0):
                count += 1
                if ( (j**2) != i) : 
                    count += 1
        if count > limit:
            count = power
        p_list.append(count)
    # print(p_list)
    answer = sum(p_list)
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(5, 3, 2)
    solution(10, 3, 2)
