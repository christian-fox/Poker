'''
made new maximum function because the max() function was regarding letters higher than numbers.
eg. max(['0', 'f', '10']) = 'f'
'''
def maximum(lst):
    lst2 = []
    for i in lst:
        if i.isnumeric():
            lst2.append(int(i))
    x = str(max(lst2))
    return(x)



players = 3
temp_player_info = {'name': ['rog', 'phelan', 'foxster'], 'chips': [1000, 1000, 1000],
                    'hand': {"rog's_hand": ['8 Hearts', '2 Diamonds'],
                             "phelan's_hand": ['10 Clubs', '10 Spades'],
                             "foxster's_hand": ['6 Diamonds', '7 Clubs']}}


betting = ["0" for _ in range(players)]  # = ['0','0','0']

'''
while any(k != maximum(betting) and k != 'f' for k in betting) or first_run_done == False:
    # while there is an item that is not 'f' or maximum(betting)
    for j in range(players):
        if all(k == maximum(betting) or k == 'f' for k in betting) and first_run_done == True:
            break
        elif betting[j] == 'f':
            pass
        elif any(i.isnumeric() and int(i)>0 for i in betting):  # if i != 'f' and >0 (bet placed)
            #print('yes: a bet has been placed')
            betting[j] = input("Enter " + str(maximum(betting))
                               + " to call, 'f' to fold or enter an amount to raise: ")
        else:  # option to check
            #print('no: it is possible to check')
            betting[j] = input("Enter 0 to check, 'f' to fold or enter an amount to raise: ")
        print("betting= ",betting)
    first_run_done = True
'''


''' TASK: if player folds, dont just replace the item with 'f', add 'f' to the end of the str.
    Then do: if item contains 'f', take away the number, and dont include in next betting round.
    How will I not include in next betting round? - if item contains 'f': pass
'''
'''
    ^^^^ Another idea would be to just take all bets off the chip stacks after each iteration.
    Lets see if this works.
'''

# function which decides if betting has finished:
def bets_settled(lst):
    settled = [False for _ in range(len(lst))]
    final = True
    for k in range(len(lst)):
        if lst[k] == maximum(lst):  # if k != max
            settled[k] = True
        elif lst[k].find('f') > -1:  # if 'f' does appear in k, ie. player has folded
            settled[k] = True
    if any(x == False for x in settled):
        final = False
    return final  # TRUE if betting is over

''' IDEA: to enter c to check -> would eliminate the need fot the 'first_run_done' variable'''



def betting_round(betting=betting):
    first_run_done = False  # this variable allows the while loop to begin,
                              # so it doesnt get stuck on betting = [0,0,0]
    while bets_settled(betting) == False or first_run_done == False:
        # while any items != max(betting)  or  != 'f' somewhere in the string
        # while there is an item that is not 'f' or maximum(betting)
        for j in range(players):
            if bets_settled(betting) == True and first_run_done == True:
                # first_run_done = True shows everyone must have checked.
                break
            elif 'f' in betting[j]:
                pass
            elif any(i.isnumeric() and int(i)>0 for i in betting):  # if i != 'f' and >0 (bet placed)
                # ie. if anything in the list is not '0' or 'f'
                decision = input("Enter " + str(int(maximum(betting)) - int(betting[j]))
                                   + " to call, 'f' to fold or enter an amount to raise: ")
                if decision.isnumeric() == True:  # if decision is numeric <-could be decimal -> bug
                    betting[j] = str(int(betting[j]) + int(decision))
                              # v. confusing way of doing item + input ie. 0 + 50
                elif decision == 'f':
                    betting[j] = betting[j] + decision
                else:
                    print("typo? try again")
                    # need to re-iterate for value of j here
            else:  # option to check
                betting[j] = input("Enter 0 to check, 'f' to fold or enter an amount to raise: ")
        first_run_done = True
    print("betting = ", betting)

    # moving bets into pot
    for p in range(players):
        if 'f' in betting[p]:
            betting[p] = betting[p].replace('f','')  # removes the 'f' from the string
            
        temp_player_info['chips'][p] -= int(betting[p])  # subtracting each players chips
    #print(temp_player_info['chips'])
    return print(temp_player_info['chips'])

betting_round()









