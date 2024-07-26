from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    name_dict = defaultdict(lambda: None)

    for i, n in enumerate(name):
        name_dict[n] = yearning[i]
    
    for name_arr in photo:
        temp_sum = 0
        for n in name_arr:
            if name_dict[n] is not None:
                temp_sum += name_dict[n]
        answer.append(temp_sum)
    print(answer)
    return answer

if __name__ == "__main__":
    solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
