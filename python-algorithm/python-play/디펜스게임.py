from collections import deque
# 시간 초과
def solution2(n, k, enemy):
    answer = 0
    q = deque()
    q.append([n,k,0])
    enemy_len = len(enemy)

    while q:
        # print(q)
        round = q.popleft()
        curr_army = round[0]
        curr_invincible = round[1]
        curr_step = round[2]
        # print(curr_army, curr_invincible, curr_step)
        if curr_step == enemy_len:
            answer = curr_step
            continue
        if enemy[curr_step] > curr_army and curr_invincible == 0:
            if answer < curr_step:
                answer = curr_step
        if enemy[curr_step] <= curr_army:
            q.append([curr_army - enemy[curr_step], curr_invincible, curr_step+1])
        if curr_invincible != 0:
            q.append([curr_army, curr_invincible-1, curr_step+1])
        
    # print(answer)
    return answer



import heapq

# 21번 문제 안풀림.
def solution3(n, k, enemy):
    answer = 0
    defeated = []
    army = n
    invincible = k
    round = 0
    for i, e in enumerate(enemy):
        # print(i, e, army, invincible)
        if e <= army:
            heapq.heappush(defeated,-e)
            army -= e
            round += 1
        else:
            if invincible != 0:
                if len(defeated) != 0:
                    if e <= army - defeated[0]:
                        a = heapq.heappop(defeated)
                        army -= a
                        army -= e
                        heapq.heappush(defeated,-e)
                invincible -= 1
                round += 1
            else:
                break
                        
    answer = round
    # print(answer)
    return answer


def solution(n, k, enemy):
    answer = 0
    defeated = []
    army = n
    invincible = k
    round = 0
    for i, e in enumerate(enemy):
        # print(i, e, army, invincible)
        heapq.heappush(defeated,e*(-1))
        army -= e
        while invincible != 0 and army < 0:    
            # print(e, army, -defeated[0] )
            army -= heapq.heappop(defeated)
            invincible -= 1
        if army < 0:
            break
        round += 1

    answer = round
    # print(answer)
    return answer


if __name__ == "__main__":
    print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]) == 5)
    print(solution(7, 3, [4, 2, 4, 5, 3, 2, 1]) == 6)
    print(solution(2, 4, [3, 3, 3, 3]) == 4)
    print(solution(2, 4, [2, 3, 3, 3, 3]) == 5)
    print(solution(2, 4, [3, 3, 3, 3, 2]) == 5)
    print(solution(2, 4, [1, 1, 3, 3, 3, 3]) == 6)
    print(solution(2, 4, [1, 1, 1, 3, 3, 3, 3]) == 6)
    print(solution(7, 3, [1, 2, 3, 4, 5, 6, 7]) == 6)
    print(solution(7, 3, [7, 6, 5, 4, 3, 2, 1]) == 5)
