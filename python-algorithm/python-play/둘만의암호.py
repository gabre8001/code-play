def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97,123)]
    
    for skip_char in skip:
        alphabet.remove(skip_char)
             
    alphabet_dict = {}
    for i, c in enumerate(alphabet):
        alphabet_dict[c] = i

    # print(alphabet)
    # print(alphabet_dict)
    dict_len = len(alphabet)
    for c in s:
        idx = alphabet_dict[c] + index
        if idx >= dict_len:
            while idx >= dict_len:
                idx -= dict_len
        if idx < 0:
            while idx < 0:
                idx += dict_len
        answer += alphabet[idx]
    # print(answer)
    return answer


if __name__ == "__main__":
    solution("aukks", "wbqd", 5)
