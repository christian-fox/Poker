# QUADS IMPROVEMENT
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def card_number_list(lst):
    number_list = []
    for i in range(len(lst)):
        if lst[i][1].isnumeric() == True:
            # double digit number
            number = int(lst[i][0:2])
        else:  #if lst[i][1] == ' ':
            # single digit number
            number = int(lst[i][0])
        number_list.append(number)
    return number_list

def card_number(string):  # gets the (integer) number of a single card
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)



player_hands2 = {"matt's_hand": {'cards': ['4 C', '4 S', '4 H', '4 D', '6 S', '6 D', '13 S'],
                 'handStr': [False, False, True, False, False, False, False, False, True, ["matt's_hand"]],
                 'high_card': [13, 6, 6, 4, 4]},
 "fox's_hand": {'cards': ['4 S', '4 H', '4 D', '6 S', '6 D', '6 C', '6 H'],
                'handStr': [False, False, True, False, False, False, True, False, False, ["matt's_hand"]],
                'high_card': [6, 6, 6, 6, 4]}}

print(player_hands2)





def Quads():
    for name in player_hands2:
        four_of_a_kind = False
        for num in range(2,15):  # num = 2,3,4,...,14
            if len(indices(card_number_list(player_hands2[name]['cards']), num)) == 4:
                print("4 OF A KIND BABY")
                four_of_a_kind = True

                # obtaining a list of 5 best cards at this moment
                last_quad_card_index = max({0,1,2,3,4,5,6} - set(indices(card_number_list(player_hands2[name]['cards']), num)))  # max index that is not already an index of one of the quad cards
                quad_cards = [player_hands2[name]['cards'][last_quad_card_index]]
                for index in indices(card_number_list(player_hands2[name]['cards']), num):
                    quad_cards.append(player_hands2[name]['cards'][index])
                    # need 1 more card added to the list - got the 4 cards for the 4 of a kind. need the next highest card.
                # sort into ascending order:
                quad_cards = sorted(quad_cards, key = card_number)
                print(quad_cards)
                                
        player_hands2[name]['handStr'].append(four_of_a_kind)
        if four_of_a_kind == True:
            # adding the cards to SameHandStr_dic
            SameHandStr_dic[name]['Quads'] = quad_cards
    return

Quads()












