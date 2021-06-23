def card_number(string):  # gets the (integer) number of a single card
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)


def rotate(lst, n):  # function rotates the list (backwards) n times
    return lst[n:] + lst[:n]




player_hands2 = {"fox's_hand": {'cards': ['2 H', '3 S', '4 C', '5 H', '6 H', '11 S', '13 D']},
                 "matt's_hand": {'cards': ['7 S', '7 D', '10 C', '13 D', '13 H', '13 S', '14 C']}}





last_player_standing = False
if last_player_standing == False:
    # Straight?
    def Straight():
        for name in player_hands2:
            player_hands2[name]['handStr'] = []
            print(name)
            Straight = False
            straight_dic = {1: (), 2: (), 3: (), 4: (), 5: (), 6: (), 0: ()}
            straight_index = []
            # creating a dic of tuples of adjacent cards in the players 7 cards
            for key in straight_dic:  # key = 0,1,2,...,6
                #print(key,type(key))
                #print(card_number(player_hands2[name]['cards'][key]))
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
            for n in range(len(straight_index)):
                # bug: only a few consecutive cards:
                if len(straight_index) < 5:
                    break
                rotate(straight_index,n)  # rotating through the list so every element gets a change to be index 0.
                if straight_index[1] - straight_index[0] == 1 and \
                   straight_index[2] - straight_index[0] == 2 and \
                   straight_index[3] - straight_index[0] == 3 and \
                   straight_index[4] - straight_index[0] == 4:  # 5 consecutive cards
                    print(name, "hit a straight!")
                    # remove all other cards apart from 1st 5:
                    straight_index = straight_index[:5]  # 1st 5 cards
                    Straight = True
                    player_hands2[name]['handStr'].append(Straight)
                    break
            if Straight == False:  # if, by the end of the loop, there is no straight:
                print(name, "does not contain a straight")
                player_hands2[name]['handStr'].append(Straight)
        return


    Straight()
    print(player_hands2)


















































