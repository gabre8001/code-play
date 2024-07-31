def solution(book_time):
    answer = 0
    time_dict = {}
    for i in range(0, 23*60+59):
        time_dict[i] = 0

    book_table = []
    for book in book_time:
        start_hours = int(book[0].split(":")[0])
        start_minutes = int(book[0].split(":")[1])
        end_hours = int(book[1].split(":")[0])
        end_minutes = int(book[1].split(":")[1])
        book_table.append([start_hours*60+start_minutes, end_hours*60+end_minutes+10])
    
    for bt in book_table:
        if bt[1] > 23*60+59:
            bt[1] = 23*60+59
        for i in range(bt[0], bt[1]):
            time_dict[i] += 1
    
    answer = max(list(time_dict.values()))
    # print(answer)
    return answer


if __name__ == "__main__":
    solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
    solution([["09:10", "10:10"], ["10:20", "12:20"]])
    solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]])
