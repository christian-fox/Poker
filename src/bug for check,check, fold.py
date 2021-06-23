# betting = [0,0,f] bug: moving chips to pot

players = 3
betting = ['0','0','f']
temp_player_info = {'name': ['a', 'bc', 'c'], 'chips': [1000, 1000, 1000],
                    'hand': {"a's_hand": ['8 Hearts', '13 Clubs'], "bc's_hand": ['11 Diamonds', '11 Hearts'], "c's_hand": ['12 Hearts', '8 Diamonds']}}
Pot = 60
# taking chips from players stack & moving chips to pot
for p in range(players):
    if 'f' in betting[p]:
        betting[p] = betting[p].replace('f','')  # removes the 'f' from the string
        if betting[p] == '':  # bug fix for pointless fold (check,check,fold)
            pass              # if no number prior to 'f'
        else:
            temp_player_info['chips'][p] -= int(betting[p])
            Pot += int(betting[p])
        betting[p] = betting[p] + 'f'  # adding the fold back on lol
    else:
        temp_player_info['chips'][p] -= int(betting[p])  # subtracting each players chips
        Pot += int(betting[p])
