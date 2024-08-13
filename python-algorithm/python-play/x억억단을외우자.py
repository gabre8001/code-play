from collections import defaultdict
# 하나 시간초과
def solution(e, starts):
    answer = []
    s_min = min(starts)
    multiple = defaultdict(lambda:0)
    for i in range(1,e+1):
        for j in range(i+1,e//i+1):
            if i*j > e:
                break
            multiple[i*j] += 2
    for i in range(1,e+1):
        if i**2 > e:
            break
        multiple[i**2] += 1
    s_list = []
    for i in range(s_min,e+1):
        s_list.append([i,multiple[i]])
    s_list.sort(key=lambda x: (-x[1], x[0]))
    # print(s_list)
    for s in starts:
        for ss in s_list:
            if ss[0] >= s:
                answer.append(ss[0])
                break
    # print(answer)
    return answer

# 시간 초과
def solution2(e, starts):
    answer = []
    s_list = []
    s_min = min(starts)
    for i in range(s_min,e+1):
        count = 0
        for j in range(1, int(i**(1/2)) + 1):
            if (i % j == 0):
                count += 1
                if ( (j**2) != i) : 
                    count += 1
        s_list.append([i,count])
    s_list.sort(key=lambda x: (-x[1], x[0]))
    # print(s_list)
    for s in starts:
        for ss in s_list:
            if ss[0] >= s:
                answer.append(ss[0])
                break

    # print(answer)
    return answer

if __name__ == "__main__":
    solution(8, [1,3,7])
