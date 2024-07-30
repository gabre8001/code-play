import sys

def solution(keymap, targets):
    answer = []

    for target_str in targets:
        target_sum = 0
        for char in target_str:
            temp_idx = sys.maxsize
            for key in keymap:
                try:
                    idx = key.index(char)
                    if temp_idx > idx:
                        temp_idx = idx
                except ValueError as e:
                    continue
            if temp_idx == sys.maxsize:
                target_sum = -1
                break
            target_sum += (temp_idx + 1)
        if target_sum == sys.maxsize:
            target_sum = -1
        answer.append(target_sum)
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
    solution(["AA"], ["B"])
    solution(["AGZ", "BSSS"], ["ASA","BGZ"])
