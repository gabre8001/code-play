def solution(numbers):
    answer = []
    def binary(n):
        result = []
        while n != 0:
            res = n%2
            n = n//2
            result.append(res)
        result.reverse()
        return result
        
    def check_length(n):
        while n != 1:
            if ((n-1) % 2) != 0:
                return 0
            n = (n-1) // 2
        return 1
    
    def check_leaf_tree(sub_t):
        if sub_t[1] == 0 and sub_t[0] == 0 and  sub_t[2] == 0:
            return 0, True
        if sub_t[1] == 0 and (sub_t[0] == 1 or sub_t[2] == 1):
            return 0, False
        return 1, True
    
    def merge_upper_level(all_level):
        all_len = len(all_level)
        result = []
        tree = 3
        start = 0
        end = start + tree
        
        while end <= all_len:
            # print(start, end)
            leaf, check = check_leaf_tree(all_level[start:end])
            if not check:
                return []
            result.append(leaf)
            start = end
            if start >= all_len:
                break
            result.append(all_level[start])
            start += 1
            end = start + tree
        # print("upper level", result)
        return result
    
    for n in numbers:
        bi_n = binary(n)
        # print(n, bi_n)
        
        while check_length(len(bi_n)) != 1:
            bi_n.insert(0,0)
        # print(n, bi_n)
        while len(bi_n) > 2:
            bi_n = merge_upper_level(bi_n)
            # print(n, bi_n)
        
        if len(bi_n) == 1 and bi_n[0] == 1:
            answer.append(1)
        else:
            answer.append(0)

    # print("answer",answer)
    return answer



if __name__ == "__main__":
    # solution([9, 7, 42, 5])
    solution([63, 111, 95])
    # solution([1, 2, 3, 4])
    # solution([29, 30, 31, 32])
    solution([255])
