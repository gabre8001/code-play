from itertools import permutations
import sys


def solution(picks, minerals):
    answer = 0

    start = 0
    end = 5
    next_stop = False
    fatigue = [[1,1,1], [5,1,1], [25,5,1]]# fatigue[곡괭이][광물]
    mineral_cost = {
        "diamond": 25,
        "iron": 5,
        "stone": 1
    }
    mineral_dict = {
        "diamond": 0,
        "iron": 1,
        "stone": 2
    }

    pick_sum = sum(picks) * 5
    if pick_sum < len(minerals):
        minerals = minerals[:pick_sum]

    sorted_minerals = []
    while next_stop == False:
        if end > len(minerals):
            end = len(minerals)
            next_stop = True
        sub_minerals = minerals[start:end]
        temp_sum = 0
        for m in sub_minerals:
            temp_sum += mineral_cost[m]
        # print(sub_minerals, temp_sum)
        sub_minerals.append(temp_sum)
        sorted_minerals.append(sub_minerals)
        start = end
        end += 5

    sorted_minerals.sort(key=lambda x: x[-1], reverse=True)
    print(sorted_minerals)
   
    m_idx = 0
    for pick_idx, num in enumerate(picks):
        while num != 0:
            num -= 1
            if m_idx == len(sorted_minerals):
                break
            for m in range(len(sorted_minerals[m_idx]) - 1):
                answer += fatigue[pick_idx][mineral_dict[sorted_minerals[m_idx][m]]]
            m_idx += 1
    print(answer)
    return answer


# slow one
def solution2(picks, minerals):
    answer = sys.maxsize
    n_pikcs = len(minerals)//5 + 1
    fatigue = [[1,1,1], [5,1,1], [25,5,1]]# fatigue[곡괭이][광물]
    mineral_dict = {
        "diamond": 0,
        "iron": 1,
        "stone": 2
    }
    m_number = []
    for m in minerals:
        m_number.append(mineral_dict[m])
    
    picks_arr = []
    for i, p in enumerate(picks):
        # print(i, p)
        temp = [ i for _ in range(p)]
        picks_arr+=temp
    
    # print("picks_arr",picks_arr)
    if n_pikcs > len(picks_arr):
        n_pikcs = len(picks_arr)
    nPr = permutations(picks_arr, n_pikcs)
    pick_p_set = set()
    for p in nPr:
        pick_p_set.add(p)
    # print("pick_p_set", pick_p_set)
    
    for p in pick_p_set:
        next_stop = False
        temp_sum = 0
        start = 0
        end = 5
        # print(p)
        pick_list = list(p)
        for pick in pick_list:
            # print("pick",pick)
            if next_stop:
                break
            if end > len(m_number):
                end = len(m_number)
                next_stop = True
            sub_minerals = m_number[start:end]
            for m in sub_minerals:
                # print(pick, m, fatigue[pick][m])
                temp_sum += fatigue[pick][m]
        
            start = end
            end += 5
        # print("temp_sum", temp_sum)
        if answer > temp_sum:
            answer = temp_sum

    # print("answer",answer)
    return answer


if __name__ == "__main__":
    solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
    solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])
