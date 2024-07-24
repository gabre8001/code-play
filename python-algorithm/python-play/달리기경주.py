def solution(players, callings):
    answer = []
    idx_player = {i: players[i] for i in range(len(players))}
    player_idx = {players[i]: i for i in range(len(players))}

    for call_player in callings:
        player1_index = player_idx[call_player]
        player1 = idx_player[player1_index]
        player2 = idx_player[player1_index-1]
        idx_player[player1_index] = player2
        idx_player[player1_index-1] = player1
        player_idx[player1] = player1_index-1
        player_idx[player2] = player1_index

    answer = list(idx_player.values())
    print(answer)
    return answer


if __name__ == "__main__":
    solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])
