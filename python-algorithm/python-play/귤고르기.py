from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    t_max = max(tangerine)
    t_dict = defaultdict(lambda:0)

    for t in tangerine:
        t_dict[t] += 1
    
    t_dict = sorted(t_dict.items(), key=lambda x: x[1], reverse=True)

    temp_sum = 0
    for t in t_dict:
        temp_sum += t[1]
        answer += 1
        if temp_sum >= k:
            break

    # print(answer)
    return answer



from itertools import combinations
# 시간 초과
def solution2(k, tangerine):
    answer = len(tangerine) + 1
    t_combi = list(combinations(tangerine, k))

    for t in t_combi:
        t_len = len(set(t))
        if answer > t_len:
            answer = t_len

    # print(answer)
    return answer



if __name__ == "__main__":
    solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
    solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
    solution(2, [1, 1, 1, 1, 2, 2, 2, 3])
