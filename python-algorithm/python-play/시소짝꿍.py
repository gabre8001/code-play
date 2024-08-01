from itertools import combinations
from collections import defaultdict

# dictionary is fast
def solution(weights):
    answer = 0
    weights_dict = defaultdict(lambda:0)

    for weight in weights:
        weights_dict[weight] += 1
    
    for weight in weights:

        if weights_dict[weight] > 1:
            answer += (weights_dict[weight] -1)

        if weight * 2 in weights_dict:
              answer += weights_dict[weight*2]
        
        if weight % 2 == 0 and weight / 2 in weights_dict:
            answer += weights_dict[weight/2]

        if weight * 2 % 3 == 0 and weight * 2 / 3 in weights_dict:
              answer += weights_dict[weight*2/3]
        
        if weight * 3 % 2 == 0 and weight * 3 / 2 in weights_dict:
            answer += weights_dict[weight*3/2]
        
        if weight * 3 % 4 == 0 and weight * 3 / 4 in weights_dict:
            answer += weights_dict[weight*3/4]
        
        if weight * 4 % 3 == 0 and weight * 4 / 3 in weights_dict:
            answer += weights_dict[weight*4/3]


    return answer/2




# slow one
def solution2(weights):
    answer = 0
    weights.sort()
    combi = list(combinations(weights, 2))
    # print(combi)
    def check_buddy(a,b):
        sub = b - a
        if sub == 0:
            return True
        elif sub == a:
            return True
        elif sub * 3 == b:
            return True
        elif sub * 4 == b:
            return True
        return False
    
    for c in combi:
        # print(c[0], c[1])
        if check_buddy(c[0], c[1]):
            answer += 1

    # print(answer)
    return answer



if __name__ == "__main__":
    print(solution([100,180,360,100,270]))
