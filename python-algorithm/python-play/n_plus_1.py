def solution(coin, cards):
    answer = 0
    cards_len = len(cards)
    current = cards_len//3
    hands_cards = cards[:current]

    def find_my_hands(hands_card):
        # print("find_my_hands",  hands_card)
        for c in hands_card:
            if (cards_len - c + 1) in hands_card:
                hands_card.remove(c)
                hands_card.remove(cards_len - c + 1)
                return hands_card, True
        return hands_card, False
    
    def is_pair_card(card1, card2):
        # print("card1",  card1, "card2", card2)
        if (cards_len - card1 + 1) == card2:
            return True
    
    def is_pair_with_card(hands_card, card):
        # print("find_my_hands",  hands_card)
        if (cards_len - card + 1) in hands_card:
            return True
    
    def is_pair(hands_card):
        # print("find_my_hands",  hands_card)
        for c in hands_card:
            if (cards_len - c + 1) in hands_card:
                return True

    def next_round(round, coin, current, hands_card):
        # print(hands_card)
        round += 1
        if len(hands_card) == 0:
            return round
        card1 = cards[current]
        current += 1
        card2 = cards[current]
        current += 1
        
        coin1 = coin - 1
        coin2 = coin - 2

        round_arr = []

        if is_pair(hands_card=hands_card):
            hands_card0 = hands_card[:]# deep copy
            next_hands_card0, result = find_my_hands(hands_card=hands_card0)
            if result or len(hands_card) > len(next_hands_card0):
                round_arr.append(next_round(round, coin, current, next_hands_card0))
        
        if coin1 > -1:
            if is_pair_with_card(hands_card=hands_card, card=card1):
                hands_card1 = hands_card[:]
                hands_card1.append(card1)
                next_hands_card1, result = find_my_hands(hands_card=hands_card1)
                if result or len(hands_card) > len(next_hands_card1):
                    round_arr.append(next_round(round, coin1, current, next_hands_card1))

            if is_pair_with_card(hands_card=hands_card, card=card2):
                hands_card2 = hands_card[:]
                hands_card2.append(card2)
                next_hands_card2, result = find_my_hands(hands_card=hands_card2)
                if result or len(hands_card) > len(next_hands_card2):
                    round_arr.append(next_round(round, coin1, current, next_hands_card2))
        
        if coin2 > -1:
            if is_pair_card(card1=card1, card2=card2):
                hands_card3 = hands_card[:]# deep copy
                round_arr.append(next_round(round, coin2, current, hands_card3))
            else:
                hands_card3 = hands_card[:]
                hands_card3.append(card1)
                hands_card3.append(card2)
                next_hands_card3, result = find_my_hands(hands_card=hands_card3)
                if result or len(hands_card) > len(next_hands_card3):
                    round_arr.append(next_round(round, coin2, current, next_hands_card3))
        
        # print("round arr", round_arr)
        if len(round_arr) == 0:
            return round

        return max(round_arr)

    answer = next_round(0, coin, current, hands_cards)
    
    # print(answer)
    return answer


if __name__ == "__main__":
    solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])
    solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12])
    solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7])
    solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
