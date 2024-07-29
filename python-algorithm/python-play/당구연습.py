import sys

def solution(m, n, startX, startY, balls):
    answer = []
    # point = [startX, startY]

    for b in balls:
        temp_point = []
        temp_point.append([2*m - startX, startY])
        temp_point.append([startX * -1, startY])
        temp_point.append([startX, 2*n - startY])
        temp_point.append([startX, startY * -1])
        if startX == startY and b[0] == b[1]:
            if startX < b[0]:
                temp_point.append((b[0] + startX)**2 + (b[1] + startY)**2)
            if startX > b[0]:
                temp_point.append((b[0] + 2*m-startX)**2 + (b[1] + 2*n-startY)**2)
        if startX == startY*-1 and b[0] == b[1]*-1:
            if startX < b[0]:
                temp_point.append((b[0] + startX)**2 + (b[1] + 2*n-startY)**2)
            if startX > b[0]:
                temp_point.append((b[0] + 2*m-startX)**2 + (b[1] + startY)**2)
        len = sys.maxsize
        for t in temp_point:
            if (startX < b[0] and b[0] < t[0] and t[1] == b[1]) or (t[0] < b[0] and b[0] < startX and t[1] == b[1]):
                continue
            if (startY < b[1] and b[1] < t[1] and t[0] == b[0]) or (t[1] < b[1] and b[1] < startY and t[0] == b[0]):
                continue
            # print(b[0], b[1], t[0], t[1])
            temp_len = (b[0] - t[0])**2 + (b[1] - t[1])**2
            if len > temp_len:
                len = temp_len
        answer.append(len)
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]])
