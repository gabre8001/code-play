def solution(friends, gifts):
    gift_mat = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for g in gifts:
        giver = g.split(" ")[0]
        taker = g.split(" ")[1]
        gift_mat[friends.index(giver)][friends.index(taker)]  += 1
    
    score = [0 for _ in range(len(friends))]
    
    for i, give in enumerate(gift_mat):
        for j, take in enumerate(gift_mat[i]):
            score[i] += (gift_mat[i][j] - gift_mat[j][i])
    
    result = [0 for _ in range(len(friends))]
    for i, give in enumerate(gift_mat):
        for j, take in enumerate(gift_mat[i]):
            if gift_mat[i][j] > gift_mat[j][i]:
                result[i] += 1
            if gift_mat[i][j] == gift_mat[j][i]:
                if score[i] > score[j]:
                    result[i] += 1
    
    return max(result)


if __name__ == "__main__":
    result = solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
    print(result)
