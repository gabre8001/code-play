def solution(s):
    answer = 0
    pre_c = s[0]
    c_count = 1
    not_c_count = 0
    idx = 1
    while idx < len(s):
        curr_c = s[idx]
        if curr_c == pre_c:
            c_count += 1
        else:
            not_c_count += 1
        idx += 1
        # print(pre_c, curr_c, c_count, not_c_count)
        if idx >= len(s):
                break
        if not_c_count != 0 and c_count == not_c_count:
            pre_c = s[idx]
            c_count = 1
            not_c_count = 0
            answer += 1
            idx += 1
    answer += 1
    # print(answer)
    return answer



if __name__ == "__main__":
    solution("banana")
    solution("abracadabra")
    solution("aaabbaccccabba")
