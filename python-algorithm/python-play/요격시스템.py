def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    # print(targets)
    end = 0
    for t in targets:
        if end <= t[0]:
            answer += 1
            end = t[1]
        
    # print(answer)
    return answer



if __name__ == "__main__":
    solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])
