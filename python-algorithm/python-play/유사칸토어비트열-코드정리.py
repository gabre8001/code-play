def solution(n, l, r):
    answer = 0

    def find_position_list(position):
        result = []
        # print("position", position)
        p_n = 0
        while 5**p_n < position:
            p_n+=1
        
        if position == 0 or position == 1:
            p_n = 1
        
        # print("p_n", p_n)

        while p_n != 0:
            p_n_idx = 0
            while 5**(p_n-1) * p_n_idx < position:
                p_n_idx+=1
            position -= 5**(p_n-1) * (p_n_idx-1)
            # print("find_position_list", p_n, p_n_idx, position)
            p_n -= 1
            # print("find_position_list", p_n, p_n_idx, position)
            result.append([p_n, p_n_idx])

        return result

    def get_one_count(p_list):
        result = 0
        zero_zone = False
        for p in p_list:
            num = p[1]
            if zero_zone:
                continue
            if p[0] != 0:
                if num == 1 or num == 2:
                    num -= 1
                elif num == 4 or num == 5:
                    num -=2
                elif num == 3:
                    num -= 1
                    zero_zone = True
            elif p[0] == 0:
                if  num == 3 or num == 4 or num == 5:
                    num -= 1
            result += 4**p[0] * num

        return result

    l_list = find_position_list(l-1)
    r_list = find_position_list(r)
    # print("l_list", l_list)
    # print("r_list", r_list)
    l_one = get_one_count(l_list)
    r_one = get_one_count(r_list)
    answer = r_one - l_one
    # print(l_one, r_one, answer)
    return answer


# 시간초과
def solution2(n, l, r):
    answer = 0
    bit_str = "1"
    idx = 0

    while idx != n:
        idx += 1
        temp_str = ""
        for c in bit_str:
            if c == "1":
                temp_str += "11011"
            else:
                temp_str += "00000"
        bit_str = temp_str

    # print(bit_str)
    sub_str = bit_str[l-1:r]
    for c in sub_str:
        if c == "1":
            answer += 1
    # print(answer)
    return answer


if __name__ == "__main__":
    # solution(1, 1, 5)
    # solution(1, 2, 5)
    # solution(1, 3, 5)
    # solution(1, 4, 5)
    # solution(1, 5, 5)
    # solution(1, 1, 4)
    # solution(1, 2, 4)
    # solution(1, 3, 4)

    # solution(2, 1, 25)
    # solution(2, 1, 24)
    # solution(2, 1, 23)
    # solution(2, 1, 22)
    # solution(2, 1, 21)
    # solution(2, 1, 20)
    # solution(2, 1, 19)
    # solution(2, 1, 18)
    # solution(2, 1, 17)
    # solution(2, 1, 16)
    # solution(2, 1, 15)
    # solution(2, 1, 14)
    # solution(2, 1, 13)
    # solution(2, 1, 12)
    # solution(2, 1, 11)
    # solution(2, 1, 10)
    # solution(2, 1, 9)
    # solution(2, 1, 8)
    # solution(2, 1, 7)
    # solution(2, 1, 6)
    # solution(2, 1, 5)
    # solution(2, 1, 4)
    # solution(2, 1, 3)
    # solution(2, 1, 2)
    solution(2, 1, 1)


    # solution(2, 3, 17)
    # solution(2, 10, 17)
    # solution(2, 11, 17)
    # solution(2, 11, 15)
    # solution(3, 124, 125)
