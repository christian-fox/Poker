players = ["i","j","k"]
names = ['matt','fox','rog']
for x in range(len(names)):
    print(players[x], names[x])


high_card_dic = {'matt': [13,12,9,6,5], 'fox': [13,12,10,6,5], 'rog': [13,12,6,5,3]}

player_hands2 = {"matt's_hand": {'cards': ['7 S', '7 D', '10 C', '13 D', '13 H', '13 S', '14 C'],
                                 'handStr': [False, False, False, True, False, False, True, False, True],
                                 'high_card': [13, 13, 13, 12, 10]},
                 "jeff's_hand": {'cards': ['6 S', '7 S', '8 S', '9 S', '14 S', '14 C', '14 H'],
                                'handStr': [False, False, False, False, True, False, True, False, False],
                                 'high_card': [13, 13, 12, 12, 11]},
                 "fox's_hand": {'cards': ['6 S', '7 S', '8 S', '9 S', '14 S', '14 C', '14 H'],
                                'handStr': [False, False, False, False, True, False, True, False, False],
                                 'high_card': [14, 13, 13, 9, 8]}}


'''
for x in high_card_dic:
    print(x)
    #for y in range(len(x)):
        #print(x[y])

for k in high_card_dic.items():
    print(k,type(k))
    var_name = k[1]
'''  
    
'''
high_card_d = {}
for names in player_hands2:
    var_name = "%s_cards" % names
    high_card_d[var_name] = player_hands2[names]['high_card']
    

print(high_card_d)
'''

high_card_player = [name for name in player_hands2]  # player list - change to names in temp player info

for j in range(5):  # j = 0,1,2,3,4  # itrating through 5 highest cards
    test_cards = []  # each players 1st highest card, 2nd highest, 3rd ...
    for name in player_hands2:
        if len(high_card_player) > 1: 
            if name in high_card_player:  # doesnt add card if player has already been 'eliminated'
                test_cards.append(player_hands2[name]['high_card'][j])
        else:  # breaks when only 1 player left in high_card_player
            break
        
    for x in range(len(test_cards)):  
        if test_cards[x] != max(test_cards):  # if card != the highest card (in this iteration)
            high_card_player.pop(x)  # remove player from the running/competition
print(high_card_player)





