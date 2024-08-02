def solution(storey):
    answer = 0
    num = str(storey)
    num_list = list(num)
    num_list.reverse()
    num_list.append(0)
    upper = 0
    for i, num in enumerate(num_list):
        n = int(num)
        n += upper
        # print(n)
        if n > 5:
            answer += (10 - n)
            upper = 1
        elif n == 5:
            if int(num_list[i+1]) > 4:
                answer += (10 - n)
                upper = 1
            else:
                answer += n
                upper = 0
        else:
            answer += n
            upper = 0
    print("answer",answer)
    return answer



if __name__ == "__main__":
    solution(16)
    solution(2554)
    solution(1)
    solution(485)
    solution(48555)
