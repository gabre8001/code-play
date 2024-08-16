from collections import deque
# BFS
def solution(n, m, x, y, r, c, k):
    go_to = [[1,0,'d'],[0,-1,'l'],[0,1,'r'],[-1,0,'u']]
    queue = deque()
    queue.append([x,y,""])

    dist = abs(r - x) + abs(c - y)
    # k 번의 이동으로 도달할 수 없는 경우
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"

    while queue:
        go_from = queue.popleft()
        for to in go_to:
            r_to = go_from[0] + to[0]
            c_to = go_from[1] + to[1]
            str_to = go_from[2] + to[2]
            # print(r_to, c_to, str_to)
            if len(str_to) > k:
                break
            if r_to == r and c_to == c and len(str_to) == k:
                # print(str_to)
                return str_to
            dist = abs(r - r_to) + abs(c - c_to)
            if dist > k - len(str_to) or (k- len(str_to) - dist) % 2 != 0:
                continue
            if 0 < r_to <= n and 0 < c_to <= m:
                queue.append([r_to,c_to,str_to])
                break
    
    # print("impossible")
    return "impossible"
    

if __name__ == "__main__":
    solution(3,4,2,3,3,1,5)
    solution(2,2,1,1,2,2,2)
    solution(3,3,1,2,3,3,4)
    solution(3,4,2,3,1,2,2)
