# function to find all occurences of an element in a list
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

'''
 Description: Creating a dictionary that stores the numbers and suits of the players hands.
'''
'''
 TO DO:
 1. change it for a variable number of players: players = 3
 2. ^ could use the var_name = %s_hand % name thing - create a new variable and store in a dic
 3. add the players hand and the table cards to the dict
 4. what arguments do i need in the function?
'''
players = 3
temp_player_info = {'name': ['matt', 'fox', 'rog'], 'chips': [1000, 1000, 1000],
 'hand': {"matt's_hand": ['14 Clubs', '10 Spades'],
          "fox's_hand": ['8 Diamonds', '10 Hearts'],
          "rog's_hand": ['4 Diamonds', '5 Clubs']}}

table_cards_list = ['13 Hearts', '13 Spades', '4 Spades', '6 Diamonds', '8 Clubs']


player_hands = {}
player_hands['card_numbers'] = {}  # sub-dic that will contain the keys: card_numbers, card_suits
player_hands['card_suits'] = {}
'''
Description: Arranges player hands into a dictionary of lists of players cards + table cards
'''
def arrange_hands():
        # here: want to append the table_cards_list to the player_hands dictionary.
        # player_hands['card_suits']["%s's_hand" % name] += [table_card_suits]
        # player_hands['card_numbers']["%s's_hand" % name] += [table_card_numbers]
        # need to split the numbers and suits first:
    table_card_dic = {}
    table_card_dic['card_numbers'] = []
    table_card_dic['card_suits'] = []
    for card in range(len(table_cards_list)):  # card = 0, 1, 2, 3, 4  -> 5 table card index's
        if table_cards_list[card][1] == ' ':
            # single digit number
            table_card_dic['card_numbers'].append(int(table_cards_list[card][0]))
            table_card_dic['card_suits'].append(table_cards_list[card][2])
        if table_cards_list[card][1].isnumeric() == True:
            # double digit number
            table_card_dic['card_numbers'].append(int(table_cards_list[card][0:2]))
            table_card_dic['card_suits'].append(table_cards_list[card][3])


    # adding each players hand to the list..
    for name in temp_player_info['name']:
        # 1st card
        if temp_player_info['hand']["%s's_hand" % name][0][1] == ' ':  # if the 2nd item in jeffs first card (string) = ' '.
            # single digit number
            first_card_number = int(temp_player_info['hand']["%s's_hand" % name][0][0])
            first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][2]
        if temp_player_info['hand']["%s's_hand" % name][0][1].isnumeric() == True:  # 1st card, 2nd item in string isnumeric
            # double digit number
            first_card_number = int(temp_player_info['hand']["%s's_hand" % name][0][0:2])
            first_card_suit = temp_player_info['hand']["%s's_hand" % name][0][3]
        # 2nd card
        if temp_player_info['hand']["%s's_hand" % name][1][
            1] == ' ':  # notice the 2nd last sq. bracket refers to the 2nd card
            # single digit number                                        # and the last sq. bracket refers to the index: 1
            second_card_number = int(temp_player_info['hand']["%s's_hand" % name][1][0])
            second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][2]
        if temp_player_info['hand']["%s's_hand" % name][1][1].isnumeric() == True:
            # double digit number
            second_card_number = int(temp_player_info['hand']["%s's_hand" % name][1][0:2])
            second_card_suit = temp_player_info['hand']["%s's_hand" % name][1][3]

            # add to dic
        player_hands['card_numbers'][
            "%s's_hand" % name] = []  # resetting the card numbers and suits 'dummy' variables for each player iteration
        player_hands['card_suits']["%s's_hand" % name] = []
        player_hands['card_numbers']["%s's_hand" % name].append(first_card_number)  # adding each players card numbers
        player_hands['card_numbers']["%s's_hand" % name].append(second_card_number)
        player_hands['card_suits']["%s's_hand" % name].append(first_card_suit)  # adding each players card suits
        player_hands['card_suits']["%s's_hand" % name].append(second_card_suit)
    
        player_hands['card_numbers']["%s's_hand" % name] += table_card_dic['card_numbers']  # adding table cards
        player_hands['card_suits']["%s's_hand" % name] += table_card_dic['card_suits']
            
    return player_hands




    '''
    print(temp_player_info['hand'])
    print(player_hands)
    '''
    # Need to add table_cards to each hand in the list
   # table_cards_list = table_cards['flop'] + table_cards['turn'] + table_cards['river']
   # print(table_cards_list)

    # changing the strings of table cards from '8 of Clubs' -> 8 C
    # then add it to each player in player_hands dictionary
    '''
    IDEA: could make the above into a function that changes a list of x cards, (and y players?) into a dictionary of numbers and suits
    '''
arrange_hands()
print(player_hands)








########################################################################################################

'''
Description: Same as player_hands() func apart from this one doesnt split card_number and card_suit.
'''



def arrange_hands2():  # dont use dictionary, join temp_player_info['hand'][%ss_hand % name][0:3] -> if single digit
                                                                                        #   [0:4] -> if double digit

    global player_hands2                                                                                 
    player_hands2 = {}
    player_hands2['cards'] = {}  # sub-dic that will contain the keys: cards
    simplified_table_cards = []                                                             
    for card in range(len(table_cards_list)):  # card = 0, 1, 2, 3, 4  -> 5 table card index's
        if table_cards_list[card][1] == ' ':
            # single digit number
            simplified_table_cards.append(table_cards_list[card][0:3])

        if table_cards_list[card][1].isnumeric() == True:
            # double digit number
            simplified_table_cards.append(table_cards_list[card][0:4])

    # adding player hands
    for name in temp_player_info['name']:
        # 1st card
        if temp_player_info['hand']["%s's_hand" % name][0][1] == ' ':  # if the 2nd item in jeffs first card (string) = ' '.
            # single digit number
            first_card = temp_player_info['hand']["%s's_hand" % name][0][0:3]
        if temp_player_info['hand']["%s's_hand" % name][0][1].isnumeric() == True:  # 1st card, 2nd item in string isnumeric
            # double digit number
            first_card = temp_player_info['hand']["%s's_hand" % name][0][0:4]
        # 2nd card
        if temp_player_info['hand']["%s's_hand" % name][1][1] == ' ':  # notice the 2nd last sq. bracket refers to the 2nd card
            # single digit number                                        # and the last sq. bracket refers to the index: 1
            second_card = temp_player_info['hand']["%s's_hand" % name][1][0:3]
        if temp_player_info['hand']["%s's_hand" % name][1][1].isnumeric() == True:
            # double digit number
            second_card = temp_player_info['hand']["%s's_hand" % name][1][0:4]

            # add to dic
        player_hands2['cards']["%s's_hand" % name] = []  # resetting the cards 'dummy' variables for each player iteration
        player_hands2['cards']["%s's_hand" % name].append(first_card)  # adding each players card numbers
        player_hands2['cards']["%s's_hand" % name].append(second_card)
        player_hands2['cards']["%s's_hand" % name] += simplified_table_cards  # adding table cards
            
    return player_hands2




     
arrange_hands2()
print(player_hands2)


########################################################################################




'''
royal_straight = {}
royal_straight['card_numbers'] = {}  # sub-dic that will contain the keys: [all players names]
royal_straight['card_suits'] = {}

for name in temp_player_info['name']:
    # does the card_number list contian 10,J,Q,K,A?
        
    for x in range(10,15):  # adds indices of all 10s,11s,12s,13s and 14s to a new 'royal flush potential' list: royal_straight
        royal_straight['card_numbers']["%s's_hand" % name] += indices(player_hands['card_numbers']["%s's_hand" % name], x)  
    print(royal_straight)
'''







