
''' obj:
try to eliminate the use of the best_hand dictionary,
and add a 'best_hand_index' key to player_hands2.

'''





jeff = 1




if jeff == 1: # cba undo-ing the indent..

    player_hands2 = {"b's_hand": {'cards': ['2 S', '2 H', '2 C', '3 D', '7 C', '8 D', '12 D'],
                                  'handStr': [False, False, False, False, False, False, False, False, False, ["a's_hand"]],
                                  'high_card': [12, 8, 7, 3, 2]},
                     "a's_hand": {'cards': ['2 H', '2 C', '3 D', '4 H', '8 C', '8 D', '12 D'],
                                  'handStr': [False, False, False, False, False, False, True, False, False, ["a's_hand"]],
                                  'high_card': [12, 8, 8, 4, 3]}}
    print(player_hands2)
    # Each players best hand:
    high_card = []
    for name in player_hands2:  # getting a list of handStr index - morph handStr key's.
        player_hands2[name]['best_hand_index'] = None
        try:
            player_hands2[name]['best_hand_index'] = player_hands2[name]['handStr'].index(True)  #
        except ValueError:  # ValueError because of the last HighCard() adds a list of names to the 'handStr' key
            player_hands2[name]['best_hand_index'] = 10  # 10 is for high_card
            
        high_card_players = player_hands2[name]['handStr'][-1]
    print('\n',player_hands2,'\n')
        
    if any(v < 10 for k,v in player_hands2.items()) == True:  
        print('we got a hand better than high_card')
        best_hand_index = min(best_hand.values())  # best hand index
        for k,v in best_hand.items():
            if v != best_hand_index:  # if the players best hand != best hand index
                player_hands2.pop(k, None)  # delete the players who dont make the cut from player_hands2
            if len(player_hands2) == 1:
                print('winner is: ', player_hands2.keys())
                break
        print('well done,', [key for key in player_hands2.keys()][0])  # <- how to print the first key in the dict
    else:
        print('all False')
        print('winner(s): ', high_card_players)
















        
