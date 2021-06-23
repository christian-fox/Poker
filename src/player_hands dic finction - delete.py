'''
 Description: Creating a dictionary that stores the numbers and suits of the players hands.
 '''
player_hands = {}
player_hands['card_numbers'] = {}  # sub-dic that will contain the keys: card_numbers, card_suits
player_hands['card_suits'] = {}
for name in temp_player_info['name']:
    # 1st card
    if temp_player_info['hand']["%s's_hand" % name][0][1] == ' ':  # if the 2nd item in jeffs first card (string) = ' '.
        # single digit number
        first_card_number = int(temp_player_info['hand']["%s's_hand" % name][0][0])
        first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][2]
    if temp_player_info['hand']["%s's_hand" % name][0][1].isnumeric() == True:  # 1st card, 2nd item in string isnumeric
        first_card_number = int(
            temp_player_info['hand']["%s's_hand" % name][0][0] + temp_player_info['hand']["%s's_hand" % name][0][1])
        first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][3]

    # 2nd card
    if temp_player_info['hand']["%s's_hand" % name][1][
        1] == ' ':  # notice the 2nd last sq. bracket refers to the 2nd card
        # single digit number                                        # and the last sq. bracket refers to the index: 1
        second_card_number = int(temp_player_info['hand']["%s's_hand" % name][1][0])
        second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][2]

    if temp_player_info['hand']["%s's_hand" % name][1][1].isnumeric() == True:
        # double digit number
        second_card_number = int(
            temp_player_info['hand']["%s's_hand" % name][1][0] + temp_player_info['hand']["%s's_hand" % name][1][1])
        second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][3]

        # add to dic
    player_hands['card_numbers'][
        "%s's_hand" % name] = []  # resetting the card numbers and suits 'dummy' variables for each player iteration
    player_hands['card_suits']["%s's_hand" % name] = []
    player_hands['card_numbers']["%s's_hand" % name].append(first_card_number)  # adding each players card numbers
    player_hands['card_numbers']["%s's_hand" % name].append(second_card_number)
    player_hands['card_suits']["%s's_hand" % name].append(first_card_suit)  # adding each players card suits
    player_hands['card_suits']["%s's_hand" % name].append(second_card_suit)

print(temp_player_info['hand'])
print(player_hands)

# Need to add table_cards to each hand in the list
print(list(table_cards.values()))
table_cards_list = table_cards['flop'] + table_cards['turn'] + table_cards['river']
print(table_cards_list)

# changing the strings of table cards from '8 of Clubs' -> 8 C
# then add it to each player in player_hands dictionary
'''
IDEA: could make the above into a function that changes a list of x cards, (and y players?) into a dictionary of numbers and suits
'''