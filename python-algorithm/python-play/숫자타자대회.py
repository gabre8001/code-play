from collections import deque
import sys


def solution(numbers):
    answer = 0
    MAX = sys.maxsize
    n_len = len(numbers)
    # tree[len][L][R]
    weight_sum = [[[MAX for _ in range(10)] for _ in range(10)] for _ in range(n_len+1)]
    weight_mat = [[MAX for _ in range(10)] for _ in range(10)]
    pad = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*','0','#']]

    def num_position(n):
        if n == 0:
            return [3,1,0]
        num = n - 1
        return [num//3, num%3, 0]

    def BFS(start, goal):
        if start[0] == goal[0] and start[1] == goal[1]:
            return 1
        move = [[-1,0,2], [1,0,2], [0,-1,2], [0,1,2], [-1,-1,3], [-1,1,3], [1,-1,3], [1,1,3]]
        q = deque()
        q.append(start)
        while q:
            # print(q)
            from_num = q.popleft()
            # print(from_num)
            for to in move:
                r_to = from_num[0] + to[0]
                c_to = from_num[1] + to[1]
                weight_to = from_num[2] + to[2]
                if r_to == goal[0] and c_to == goal[1]:
                    # print(weight_to)
                    return weight_to
                if r_to == 3 and (c_to == 0 or c_to == 2):
                    continue
                if 0 <= r_to < 4 and 0 <= c_to < 3:
                    q.append([r_to, c_to, weight_to])

    for i in range(10):
        for j in range(10):
            start = num_position(i)
            end = num_position(j)
            weight = BFS(start=start, goal=end)
            weight_mat[i][j] = weight
    # print(weight_mat)

    q = deque()
    temp = []
    q.append([4,6])
    weight_sum[0][4][6] = 0

    for i, n in enumerate(numbers):
        # print(q)
        num = int(n)
        p = num_position(num)
        while q:
            curr = q.popleft()
            l_num = curr[0]
            r_num = curr[1]
            if l_num == r_num:
                continue
            # step i weight
            l_weight = weight_mat[l_num][num]
            r_weight = weight_mat[r_num][num]
            # print(p, l_start, r_start, l_weight, r_weight)
            if weight_sum[i+1][l_num][num] == MAX:
                temp.append([l_num, num])
            if weight_sum[i+1][num][r_num] == MAX:
                temp.append([num, r_num])

            if weight_sum[i+1][l_num][num] > weight_sum[i][l_num][r_num] + r_weight:
                weight_sum[i+1][l_num][num] = weight_sum[i][l_num][r_num] + r_weight    
            if weight_sum[i+1][num][r_num] > weight_sum[i][l_num][r_num] + l_weight:
                weight_sum[i+1][num][r_num] = weight_sum[i][l_num][r_num] + l_weight
            
        q = deque(temp)
        temp = []

    answer = MAX
    for i in range(10):
        for j in range(10):
            sum = weight_sum[n_len][i][j]
            if sum != MAX and answer > sum:
                answer = sum

    # print(answer)
    return answer




# wrong solution
def solution2(numbers):
    answer = 0
    pad = [['1','2','3'], ['4','5','6'], ['7','8','9'], ['*','0','#']]
    l_start = [1,0,0] # 4
    r_start = [1,2,0] # 6

    def num_position(n):
        n = int(n)
        if n == 0:
            return [3,1,0]
        num = n - 1
        return [num//3, num%3, 0]

    def BFS(start, goal):
        if start[0] == goal[0] and start[1] == goal[1]:
            return 1
        move = [[-1,0,2], [1,0,2], [0,-1,2], [0,1,2], [-1,-1,3], [-1,1,3], [1,-1,3], [1,1,3]]
        q = deque()
        q.append(start)
        while q:
            # print(q)
            from_num = q.popleft()
            # print(from_num)
            for to in move:
                r_to = from_num[0] + to[0]
                c_to = from_num[1] + to[1]
                weight_to = from_num[2] + to[2]
                if r_to == goal[0] and c_to == goal[1]:
                    print(weight_to)
                    return weight_to
                if r_to == 3 and (c_to == 0 or c_to == 2):
                    continue
                if 0 <= r_to < 4 and 0 <= c_to < 3:
                    q.append([r_to, c_to, weight_to])

    for n in numbers:
        p = num_position(n)
        l_weight = BFS(l_start, p)
        r_weight = BFS(r_start, p)
        print(p, l_start, r_start, l_weight, r_weight)
        if l_weight < r_weight:
            answer += l_weight
            l_start = p
        else:
            answer += r_weight
            r_start = p
    print(answer)
    return answer



if __name__ == "__main__":
    solution("1756")
    solution("5123")
    solution("4646")
    solution("10252525252525")
    solution("10525252525252")
