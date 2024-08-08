from collections import deque

def solution(s):
    answer = []
    q = deque()

    for i, char in enumerate(s):
        # print(i,char, q)
        try:
            idx = q.index(char) + 1
        except ValueError as e:
            idx = -1
        answer.append(idx)
        q.appendleft(char)

    # print(answer)
    return answer


if __name__ == "__main__":
    solution("banana")
    solution("foobar")
