# Kadane's Algorithm
# 부분수열의 합을 구하는 빠른 방법
def solution(sequence):
    answer = 0
    answer = 0
    seq_len = len(sequence)
    purse1 = [1 for _ in range(seq_len)]
    purse2 = [1 for _ in range(seq_len)]
    sequence1 = []
    sequence2 = []
    sequence1_sums = []
    sequence2_sums = []
    for i in range(seq_len):
        if i % 2 == 0:
            purse1[i] = -1
        else:
            purse2[i] = -1
        sequence1.append(sequence[i] * purse1[i])
        sequence2.append(sequence[i] * purse2[i])

    # print(sequence)
    # print(sequence1)
    # print(sequence2)
    
    sequence1_sums.append(sequence1[0])
    for i in range(1,seq_len):
        sequence1_sums.append(max(sequence1[i], sequence1[i] + sequence1_sums[i-1]))
    answer1 = max(sequence1_sums)

    sequence2_sums.append(sequence2[0])
    for i in range(1,seq_len):
        sequence2_sums.append(max(sequence2[i], sequence2[i] + sequence2_sums[i-1]))
    answer2 = max(sequence2_sums)
    answer = max(answer1, answer2)
    # print(answer)
    return answer


# brute force
# 모든 가능한 부분배열을 구하기
def solution2(sequence):
    answer = 0
    seq_len = len(sequence)
    purse1 = [1 for _ in range(seq_len)]
    purse2 = [1 for _ in range(seq_len)]
    sequence1 = []
    sequence2 = []
    for i in range(seq_len):
        if i % 2 == 0:
            purse1[i] = -1
        else:
            purse2[i] = -1
        sequence1.append(sequence[i] * purse1[i])
        sequence2.append(sequence[i] * purse2[i])

    print(sequence)
    print(sequence1)
    print(sequence2)

    temp_sum = 0
    for i in range(seq_len):
        temp_sum1 = 0
        temp_sum2 = 0
        for j in range(i, seq_len):
            temp_sum1 += sequence1[j]
            if temp_sum1 > answer:
                answer = temp_sum1
            temp_sum2 += sequence2[j]
            if temp_sum2 > answer:
                answer = temp_sum2
    
    print(answer)
    return answer


if __name__ == "__main__":
    solution([2, 3, -6, 1, 3, -1, 2, 4])
