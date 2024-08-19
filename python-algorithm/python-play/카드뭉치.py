from collections import defaultdict, deque

def solution(cards1, cards2, goal):
    
    c_1_q = deque(cards1)
    c_2_q = deque(cards2)
    g_q = deque(goal)

    while g_q:
        g = g_q.popleft()
        if c_1_q and g == c_1_q[0]:
            c_1_q.popleft()
        elif c_2_q and g == c_2_q[0]:
            c_2_q.popleft()
        else:
            return "No"

    return "Yes"


if __name__ == "__main__":
    print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
    print(solution(["want", "i", "drink", "water"], ["to"], ["i", "to"]))
    print(solution( ["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"]))
    print(solution(["show", "lot", "please", "the", "me"], ["money"], ["show", "me", "the", "money"]))
