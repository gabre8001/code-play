import math

def solution(r1, r2):
    answer = 0
    small_r = r1*r1
    large_r = r2*r2

    for x in range(1, r2+1):
        # print("small_r - x*x", small_r - x*x)
        min_y = math.ceil(math.sqrt((small_r - x*x) if(small_r - x*x)>=0 else 0))
        max_y = math.sqrt(large_r - x*x)
        if max_y is not 0 and max_y.is_integer():
            max_y += 1
        else:
            max_y = math.ceil(max_y)
        # print("m, l :: ", min_y, max_y)
        answer += (max_y-min_y)
    
    answer *= 4
    
    # print(answer)
    return answer


# slow one
def solution2(r1, r2):
    answer = 0
    small = r1*r1
    large = r2*r2

    for x in range(r2+1):
        for y in range(1, r2+1):
            if small <= (x*x + y*y) and (x*x + y*y) <= large:
                answer += 1
    
    answer *= 4
    
    # print(answer)
    return answer



if __name__ == "__main__":
    solution(2,3)

    # solution(2,4)
