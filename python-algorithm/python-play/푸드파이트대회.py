def solution(food):
    answer = ''
    left = ""
    right = ""
    for i, f in enumerate(food):
        if i == 0:
            continue
        for _ in range(int(f//2)):
            left += str(i)
            right = str(i) + right
    # print(left)
    # print(right)
    answer = left + "0" + right
    return answer


if __name__ == "__main__":
    solution([1, 3, 4, 6])
    solution([1, 7, 1, 2])
