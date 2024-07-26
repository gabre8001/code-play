def solution(plans):
    answer = []
    stack = []
    plans.sort(key=lambda x: x[1])
    
    for p in plans:
        times = p[1].split(":")
        minutes = int(times[0]) * 60 + int(times[1])
        p[1] = minutes
        p[2] = int(p[2])
    now = 0

    for p in plans:
        while len(stack) != 0 and (now + stack[-1][2]) <= p[1]:
            now += stack[-1][2]
            answer.append(stack.pop()[0])
        if len(stack) == 0:
            stack.append(p)
            now = p[1]
        else:
            playtime = stack[-1][2]
            if now + playtime > p[1]:
                stack[-1][2] = playtime - (p[1] - now)
                stack.append(p)
                now = p[1] 
        # print(now, stack)
    while len(stack) != 0:
            answer.append(stack.pop()[0])
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]])
    solution([["music", "12:20", "40"], ["computer", "12:30", "100"], ["science", "12:40", "50"], ["history", "14:00", "30"] ])
    solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]])
    solution([["aaa", "11:40", "20"], ["bbb", "11:45", "5"], ["ccc", "11:50", "5"], ["ddd", "11:55", "5"], ["eee", "12:05", "5"]])
    # ["bbb", "ccc", "ddd", "eee", "aaa"]
    solution([["aaa", "11:40", "20"], ["bbb", "11:45", "5"], ["ccc", "11:50", "5"], ["ddd", "11:55", "15"], ["eee", "12:05", "10"], ["fff", "12:40", "10"]])
    # ['bbb', 'ccc', 'eee', 'ddd', 'aaa', 'fff']
