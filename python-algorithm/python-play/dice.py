from itertools import combinations

def solution(dice):
    answer = []
    dice_len = len(dice)
    dice_num = [i for i in range(dice_len)]

    a_dice = combinations(dice_num, int(dice_len/2))
    # print('len', len(list(a_dice)))
    a_dice = list(a_dice)
    
    a_case = []

    def sum_component(depth, combi, sum, case):
        if depth == len(combi) - 1:
            for n in dice[combi[depth]]:
                case.append(sum+n)
            return
        
        for n in dice[combi[depth]]:
            sum_component(depth=depth+1, combi=combi, sum=sum+n, case=case)

    a_win = 0
    for a_dices in a_dice:
        a_case = []
        sum_component(0, list(a_dices), 0, a_case)
        b_dices = [x for x in dice_num if x not in list(a_dices)]
        # print("a_dices", a_dices, "b_dices", b_dices)
        b_case = []
        sum_component(0, list(b_dices), 0, b_case)
        
        
        temp_a_win = 0
        a_idx = 0
        b_idx = 0
        case_len = len(a_case)
        a_case.sort()
        b_case.sort()
        print("a_case", a_case)
        print("b_case", b_case)
        b_idx = 0
        win = 0
        for a in a_case:
            while b_idx < case_len:
                if a > b_case[b_idx]:
                    win +=1
                    b_idx += 1
                else:
                    break
            temp_a_win += win

        if a_win < temp_a_win:
            a_win = temp_a_win
            answer = list(a_dices)
        print("temp_a_win", temp_a_win)
        print("a_win", a_win)
        print("answer", answer)
        # break
    answer.sort()
    return [x+1 for x in answer]


if __name__ == "__main__":
    result = solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])
    print("result", result)

    result = solution([[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]])
    print("result", result)

    # result = solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70],[40, 41, 42, 43, 44, 95], [43, 43, 42, 42, 41, 91], [1, 1, 80, 80, 80, 90], [70, 70, 1, 1, 70, 90]])
    # print(result)
