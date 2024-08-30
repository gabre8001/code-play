from math import gcd

def solution(arrayA, arrayB):
    answer = 0
    array_len = len(arrayA)
    gdc_a = arrayA[0]
    gdc_b = arrayB[0]

    for i in range(array_len):
        gdc_a = gcd(gdc_a, arrayA[i])
        gdc_b = gcd(gdc_b, arrayB[i])

    answer_a = gdc_a
    answer_b = gdc_b
    
    for i in range(array_len):
        if arrayA[i] % gdc_b == 0:
            answer_b = 0
            break
    
    for i in range(array_len):
        if arrayB[i] % gdc_a == 0:
            answer_a = 0
            break
        
    answer = max(answer_a, answer_b)
    if answer == 1:
        answer = 0
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([10, 17], [5, 20])
    solution([10, 20], [5, 17])
    solution([14, 35, 119], [18, 30, 102])
