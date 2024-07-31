import sys
from collections import deque

def solution(x, y, n):
    def BFS(x, y, n):
        if x == y:
            return 0
        queue = deque([(x, 0)])
        visited = set()
        visited.add(x)

        while queue:
            # print(queue)
            curr_x, step = queue.popleft()
            next_x = [curr_x+n, curr_x*2, curr_x*3]

            for nx in next_x:
                if nx == y:
                    return step + 1
                if nx < y and nx not in visited:
                    queue.append((nx, step+1))
                    visited.add(nx)

        return -1

    answer = BFS(x, y, n)
    # print(answer)
    return answer



# stack over flow...
def solution2(x, y, n):

    def dfs(step, curr_x):
        if curr_x == y:
            return step
        if curr_x > y:
            return sys.maxsize
        step += 1
        plus_n = dfs(step=step, curr_x=(curr_x+n))
        mul_2 = dfs(step=step, curr_x=(curr_x*2))
        mul_3 = dfs(step=step, curr_x=(curr_x*3))
        # print(plus_n, mul_2, mul_3)
        # print(curr_x, y, n)

        return min(plus_n, min(mul_2, mul_3))
        

    answer = dfs(0, x)
    if answer == sys.maxsize:
        answer = -1
    # print(answer)
    return answer



if __name__ == "__main__":
    solution(10, 40, 5)
    solution(10, 40, 30)
    solution(2, 5, 4)
