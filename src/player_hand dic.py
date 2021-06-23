player_hands = {}
player_hands['card_numbers'] = {}  # sub-dic that will contain the keys: card_numbers, card_suits
player_hands['card_suits'] ={}
for name in temp_player_info['name']:
    if temp_player_info['hand']["%s's_hand" % name][0][1] == ' ':
        print(temp_player_info['hand']["%s's_hand" % name][0], 'is a single digit number')
        # single digit number
        first_card_number = int(temp_player_info['hand']["%s's_hand" % name][0][0])
        second_card_number = int(temp_player_info['hand']["%s's_hand" % name][1][0])
        first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][2]
        second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][2]

    else:
        # double digit number
        first_card_number = int(temp_player_info['hand']["%s's_hand" % name][0][0] + temp_player_info['hand']["%s's_hand" % name][0][1])
        second_card_number = int(temp_player_info['hand']["%s's_hand" % name][1][0] + temp_player_info['hand']["%s's_hand" % name][1][1])
        first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][3]
        second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][3]
        
        # add to 
    #player_hands["%s's_hand" % name]['card_numbers'] = []  # creating new dictionary key: 'card_numbers'
    player_hands['card_numbers']["%s's_hand" % name] = []
    player_hands['card_suits']["%s's_hand" % name] = []
    player_hands['card_numbers']["%s's_hand" % name].append(first_card_number)  # adding each players card numbers
    player_hands['card_numbers']["%s's_hand" % name].append(second_card_number) 
    player_hands['card_suits']["%s's_hand" % name].append(first_card_suit)  # adding each players card suits
    player_hands['card_suits']["%s's_hand" % name].append(second_card_suit) 

print(temp_player_info['hand'])
print(player_hands)



### if statements are only looking at the first card.. FIX
