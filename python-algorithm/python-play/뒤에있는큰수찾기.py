
# stack is faster
def solution(numbers):
    answer = [0 for _ in range(len(numbers))]
    stack = []
    for i, n in enumerate(numbers):
        if len(stack) == 0:
            stack.append([i,n])
            answer[i] = -1
        else:
            while len(stack) != 0 and stack[-1][1] < n:
                a = stack.pop()
                answer[a[0]] = n
            stack.append([i,n])
        # print(stack)
        # print(answer)
    
    while len(stack) != 0:
        a = stack.pop()
        if answer[a[0]] == 0:
            answer[a[0]] = -1
        
    # print("answer", answer)
    return answer

# slow one
def solution2(numbers):
    answer = []
    n_len = len(numbers)
    answer_len = 0
    pre_answer_len = 0
    num_dict = {}
    for i, n in enumerate(numbers):
        num_dict[i] = n
    
    for i in range(n_len):
        pre_answer_len = answer_len
        for j in range(i+1, n_len):
            if num_dict[j] > num_dict[i]:
                answer.append(num_dict[j])
                answer_len += 1
                break
        if answer_len == pre_answer_len:
            answer.append(-1)
            answer_len += 1

    # print(answer)
    return answer


if __name__ == "__main__":
    solution([2, 3, 3, 5])
    solution([9, 1, 5, 3, 6, 2])
