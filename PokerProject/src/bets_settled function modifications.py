def maximum(lst):
    lst2 = []
    for i in lst:
        if i.isnumeric():
            lst2.append(int(i))
    x = max(lst2)
    return(str(x))

players = 4
SB_chips = 10
BB_chips = 20
betting = ["0" for _ in range(players-2)] + [str(SB_chips),str(BB_chips)]  # initial betting pot
'''Note: Can easily hard code the SB & BB chips to the end of the list as they will always
         be at the end of the list, by nature, since I have rotated UTG to be first.'''


betting = ['0','20','20','f']
'''

# function which decides if betting has finished:
def bets_settled(lst=betting):
    settled = [False for _ in range(len(lst))]
    is_betting_over = True  # bettig is over until proven otherwise
    for k in range(len(lst)):
        if settled.count(False) == 1:  # if 'False' only appears once in the list
            print("easy way out")
            return True
        if lst[k] == maximum(lst):  # if k == max
            settled[k] = True
        if lst[k].find('f') > -1:  # if 'f' does appear in k, ie. player has folded
            settled[k] = True
        print(settled)
    if settled.count(False) > 1:   # is there >1 player needing to go
        is_betting_over = False
    return is_betting_over  # TRUE if betting is over
'''
# ^^^ Trying to condense the two functions: last_player_standing() and bets_settled()




#print(bets_settled())




### OLD bets_settled() function:
# function which decides if betting has finished:
def bets_settled(lst=betting):
    settled = [False for _ in range(len(lst))]
    is_betting_over = True  # bettig is over until proven otherwise
    for k in range(len(lst)):
        if lst[k] == maximum(lst):  # if k == max
            settled[k] = True
        if lst[k].find('f') > -1:  # if 'f' does appear in k, ie. player has folded
            settled[k] = True
        print(settled)
    if any(z == False for z in settled):   # someones not settled
        is_betting_over = False
    return is_betting_over  # TRUE if betting is over


#print(bets_settled())



betting = ['40','0f','10f','20f']
# last player standing - folds function
def last_player_standing(lst=betting):
    end = False
    folded = [False for _ in range(len(lst))]
    for k in range(len(lst)):
        if lst[k].find('f') > -1:  # player folded
            folded[k] = True  
        if folded.count(False) == 1:  # if 'False' only appears once in the list
            end = True
            #winner = temp_player_info['name'][folded.index(False)]
            break 
    return end

print(last_player_standing())










