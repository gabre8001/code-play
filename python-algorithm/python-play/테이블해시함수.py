def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col-1], -x[0]))
    for i, d in enumerate(data[row_begin-1:row_end]):
        # print(i+row_begin, d)
        base = i + row_begin
        mod_sum = 0
        for num in d:
            mod_sum += num % base
        answer ^= mod_sum

    print(answer)
    return answer


if __name__ == "__main__":
    solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)
