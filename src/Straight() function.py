# STRAIGHT FUNCTION
    # 2. Straight Flsuh? -> first define function, Straight():
    
    def Straight():
        # Straight?
        for name in player_hands2:
            straight_dic = {1: (), 2: (), 3: (), 4: (), 5: (), 6: (), 0: ()}
            straight_index = []
            # creating a dic of tuples of adjacent cards in the players 7 cards
            for key in straight_dic:  # key = 0,1,2,...,6
                if key == 0: # last and first in the list - ace exception
                    straight_dic[key] = (card_number(player_hands2[name]['cards'][6]),
                                         card_number(player_hands2[name]['cards'][0]))
                straight_dic[key] = (card_number(player_hands2[name]['cards'][key-1]),
                                     card_number(player_hands2[name]['cards'][key]))
            # checking if the tuples are consecutive
            for key in straight_dic:  # key = 0,1,2,...,6
                if key == 0:  # and...
                    if straight_dic[1][0] - straight_dic[key][1] == -12:  # no combination of cards other than 2 - 14 that could = -12
                        straight_index += [straight_dic[key][1]] + [straight_dic[1][0]]
                elif straight_dic[key][1] - straight_dic[key][0] == 1:
                    straight_index += [straight_dic[key][0]] + [straight_dic[key][1]]  # adds both numbers of tuple
            # remove duplicates from straight_index:
            straight_index = list(dict.fromkeys(straight_index))  # creates a dic key for each value then morphs back into a list of each unique key
            # 5 cards in a row?
            straight = False
            for n in range(len(straight_index)):
                rotate(straight_index,n)  # rotating through the list so every element gets a change to be index 0.
                if straight_index[1] - straight_index[0] == 1 and \
                   straight_index[2] - straight_index[0] == 2 and \
                   straight_index[3] - straight_index[0] == 3 and \
                   straight_index[4] - straight_index[0] == 4:  # 5 consecutive cards
                    print(name, "hit a straight!")
                    straight = True
                    break
            if straight == False:
                print(name, "does not contain a straight")
    return player_hands2[name]['handStr'].append(Straight)
