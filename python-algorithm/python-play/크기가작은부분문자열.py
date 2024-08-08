def solution(t, p):
    answer = 0
    sub_len = len(p)
    p_int = int(p)
    start = 0
    end = sub_len
    max_len = len(t)
    while end <= max_len:
        sub = t[start:end]
        # print(sub, int(sub))
        if p_int >= int(sub):
            answer += 1
        start += 1
        end += 1

    # print(answer)
    return answer



if __name__ == "__main__":
    solution("3141592", "271")
    solution("500220839878", "7")
    solution("10203", "15")
