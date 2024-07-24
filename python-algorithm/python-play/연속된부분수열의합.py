def solution(sequence, k):
    answer = []
    seq_len = len(sequence)
    sub_seq_len = seq_len
    temp_sub_seq_len = 0
    start = 0
    end = 1
    temp_sum = sequence[start]
    while start < seq_len:
        # print("start", start, "temp_sum", temp_sum)
        if temp_sum > k:
            temp_sum -= sequence[start]
            start += 1
        elif temp_sum == k:
            temp_sub_seq_len = end - start
            if temp_sub_seq_len < sub_seq_len:
                sub_seq_len = temp_sub_seq_len
                answer = [start, end-1]
            if temp_sub_seq_len == seq_len: 
                answer = [start, end-1]
                break
            temp_sum -= sequence[start]
            start += 1
        elif temp_sum < k and end < seq_len:
            temp_sum += sequence[end]
            end +=1
        elif temp_sum < k and end == seq_len:
            temp_sum -= sequence[start]
            start += 1

    print(answer)
    return answer


def solution2(sequence, k):
    seq_len = len(sequence)
    sub_seq_len = seq_len
    answer = []
    temp_sub_seq_len = 0
    for start, n in enumerate(sequence):
        end = start
        temp_sum = 0
        while end < seq_len and temp_sum < k:
            temp_sum += sequence[end]
            end += 1
        temp_sub_seq_len = end - start
        if temp_sum == k and temp_sub_seq_len < sub_seq_len:
            sub_seq_len = temp_sub_seq_len
            answer = [start, end-1]
        if temp_sum == k and temp_sub_seq_len == seq_len:
            answer = [start, end-1]
            break

    # print(answer)
    return answer


if __name__ == "__main__":
    solution([1, 2, 3, 4, 5], 7)
    solution([1, 1, 1, 2, 3, 4, 5], 5)
    solution([2, 2, 2, 2, 2], 6)
    solution([1, 1, 1, 1, 1, 1, 1], 7)
