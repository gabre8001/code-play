
answer = [-1, -1]
def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    e_len = len(emoticons)

    def DFS(step, temp_list):
        global answer
        if e_len == step:
            temp_price_sum = 0
            temp_service = 0
            for user in users:
                temp_price = 0
                for i, dis in enumerate(temp_list):
                    # print(i,dis,emoticons[i])
                    if user[0] <= dis:
                        temp_price += emoticons[i] * (100-dis) // 100
                # print(user, temp_price)
                if user[1] <= temp_price:
                    temp_service += 1
                else:
                    temp_price_sum += temp_price
            # print(temp_service, temp_price_sum)
            # result.append([temp_service, temp_price_sum])
            if answer[0] < temp_service or (answer[0] == temp_service and answer[1] < temp_price_sum):
                answer = [temp_service, temp_price_sum]
            return
        
        for d in discount:
            temp_list.append(d)
            DFS(step=step+1, temp_list=temp_list)
            temp_list.pop()

    DFS(0,[])
    print(answer)
    return answer



if __name__ == "__main__":
    solution([[40, 10000], [25, 10000]], [7000, 9000])
    # solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])
