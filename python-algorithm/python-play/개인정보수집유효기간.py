from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    today_arr = today.split(".")
    today_dt = datetime(int(today_arr[0]), int(today_arr[1]), int(today_arr[2]))
    terms_dict = {}
    for t in terms:
        t_arr = t.split(" ")
        terms_dict[t_arr[0]] = int(t_arr[1])
    
    for i, p in enumerate(privacies):
        p_arr = p.split(" ")
        dt_arr = p_arr[0].split(".")
        month = terms_dict[p_arr[1]] + int(dt_arr[1])
        year = 0
        while month // 12 != 0:
            year = month // 12
            month = month % 12
        if month == 0:
            year -= 1
            month = 12
        # print(int(dt_arr[0]) + year, month, int(dt_arr[2]))
        p_dt = datetime(int(dt_arr[0]) + year, month, int(dt_arr[2]))
        # print(p_dt, today_dt, p_dt < today_dt)
        if p_dt <= today_dt:
            answer.append(i+1)
        # privacies_dict[p_arr[0]] = terms_dict[p_arr[1]]
    
    # print(answer)
    return answer


if __name__ == "__main__":
    solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
    solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
