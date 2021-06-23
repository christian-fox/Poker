''' POKER GAME'''
# Defining initial variables:
players = int(input("How many players? "))  # number of players




# Creating a deck of cards.
## Create a dictionary for the deck
number_int = list(range(2, 15)) # list of card numbers -> let ace = 15
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]

## this loop creates identical number list but all items are of type <str>
i = 0
number = []
for num in number_int:
    if type(num) != "<class 'str'>":  # (conditional not actually needed here)
        number.append(str(num))
        i += 1

## matching number to suit (ie. generating the 52 cards)
deck = []
for i in suit:
    for j in number:
        card = j + " " + i
        deck.append(card)

## Dealing.
import random
'''
 (this line below) Produces a list of [2*Players] cards to be dealt to the players.
 random.sample() takes a random list from the deck of cards,
 and the arg. k is the size of the list.
 The [+5] here are the 'table' cards, and will be turned over later.
'''
cards_to_be_split = random.sample(deck, k = 2*players + 5)


# Input player names and creating the player-chip dictionary.
player_info = {}  # dictionary

player_info['name'] = []

# this loop obtains the players names and prints them.
for i in range(1, players+1):
    name = input('Enter ' + 'Player' + str(i) + ' Name: ')
    player_info['name'].append(name)
    #var_name = "Player%d" % i     # var_name = Player1
    #print(var_name, 'is called', name) 


player_info['chips'] = [1000 for _ in range(players)]  # creates a list of size: player_number, with all elements = 1000


# Assigning dealer:
'''
quick fix1: choose x random numbers between 2-14 and choose random suits to go with it.
quick fix2: if there are 2 high cards, then just regenerate the high_card list.
Note: might be a bit sus how there are never any duplicated numbers drawn for this method lol
proper fix: if there are 2 high cards, then do an other round with just these people involved.
'''
## chooses 3 random numbers between 2-14.
high_card = random.sample(number_int,k=players)

## getting position of largest element in high_card list
m = high_card.index(max(high_card))
Dealer = player_info['name'][m]

### adding a random suit to each item(number) in the list.
i=0
for card in high_card:
    s = random.choice(suit)
    high_card[i] = str(card) + " " + s
    i += 1

## adding a 'hand' key to player info dictionary:
player_info['hand'] = high_card
print("To determine who gets the button, we will see who draws the highest card:")
for i in range(players):
    print(player_info['name'][i], 'gets', player_info['hand'][i])


print(Dealer,'has the highest card, so they will start as the dealer.')

## assigning blinds using modulo
SB_index = ((m+1) % players)
BB_index = ((m+2) % players)
UTG_index = ((m+3) % players)
print(UTG_index,type(UTG_index))
SB = player_info['name'][SB_index]
BB = player_info['name'][BB_index]
print("SB is", SB)
print("BB is", BB)

''' to update the dealer, just update m: m = ((m+1) % players) '''
'''Note: should probably assign a position name to everyone when assigning the dealer.'''


# Dealing the first hand:
player_info['hand'] = {}  # creates a nested/sub dictionary in the 'hand' key
for i in player_info['name']:  # if 3 players -> i=1,2,3.
    #var_name = "hand%d" % i    # this creates i variables, called hand1, hand2, hand3...
                               # the %d represents an integer. %s represents a string.
    var_name = "%s's_hand" % i 
    player_info['hand'][var_name] = cards_to_be_split[-2:]  # assigns the last 2 cards on the list to hand1.
    cards_to_be_split = cards_to_be_split[:-2]    # removes these 2 last cards from the original list.
print(player_info['hand'])



# Starting game1:
'''
make temp dictionary for game 1: temp_player_info = player_info
if player folds -> remove the player from each key of the dictionary
if player bets, move their chips to pot
'''
temp_player_info = player_info  # creates temporary player_info dictionary that i am free to manipulate
'''
will have to find a clever way to update the main dictionary at the end of the game/round
'''

###################################### PROBLEM #############################################
'''
Description: rotating the player indexes so UTG player is first.
NOTE: m is the index of the player who got the highest card
'''

### initial rearrange of the player_info dic:
def rotate(lst, n):  # function rotates the list (backwards) n times
    return lst[n:] + lst[:n]

def dic_rotate(dic, n):  # rotates the dictionary by n to the right
    dic = list(dic.items())  # converting to tuples list 
    updated_dic = [dic[(i - n) % len(dic)] for i, x in enumerate(dic)]  # performing rotate 
    updated_dic = {sub[0]: sub[1] for sub in updated_dic}  # reconverting to dictionary
    return updated_dic


## rotating all key lists in the temp-dic: (for assigned dealer)
temp_player_info['name'] = rotate(temp_player_info['name'],UTG_index)
temp_player_info['chips'] = rotate(temp_player_info['chips'],UTG_index)
temp_player_info['hand'] = dic_rotate(temp_player_info['hand'],-UTG_index)  # minus sign here because the dic_rotate function moves items forwards (opposite to the rotate func)




'''
... then I can update this dictionary each game: - make function too
 for i in range(players):
     if i == players - 1:  # last player
         temp_player_info['name'][i] = temp_player_info['name'][0]    # repeat for all keys
     else:
         temp_player_info['name'][i] = temp_player_info['name'][i+1]  # repeat for all keys

can also do this using modulo:
for i in range(players):
'''

def button_pass(dictionary):  # use this after game1 has finished !!
    dictionary['name'] = rotate(dictionary['name'],-1)
    dictionary['chips'] = rotate(dictionary['chips'],-1)
    dictionary['hand'] = dic_rotate(dictionary['hand'],1)
    return dictionary

############################################################################################


# Pot:
'''
lets let the blinds be 10,20 to start.
1st: assign these chips to a pot from the designated SB & BB.
'''
Pot = 0
SB_chips = 10
BB_chips = 20

print("Pot =", SB_chips + BB_chips)
print(temp_player_info)


# Betting rounds
############## Problem I will encounter after someone folds before the flop: ##################
'''
Say betting = [0, 100, f, 300], this would represent: P1 checks, P2 raising to 100,
then P3 folds, then P4 raises to 300.
A conditional would be needed after:
for i in betting:
    if i == 'f':
        list.remove(betting[i]) # this is for the folded players
        list.remove(temp_player_info['name'][i])
        list.remove(temp_player_info['chips'][i])
        list.remove(temp_player_info['hand']['PLayer'+i])  # need to create a sub-dic for each hand with variable variable names
'''

######################################### BETTING ROUND LOOP ##############################################

'''
Description: if player folds, add 'f' to the end of the item in 'betting' list.
    Then do: if item contains 'f', take away the number from players stack, and dont include in next betting round.
    How will I not include in next betting round? - if item contains 'f': pass
'''
def maximum(lst):
    lst2 = []
    for i in lst:
        if i.isnumeric():
            lst2.append(int(i))
    x = max(lst2)
    return(str(x))

betting = ["0" for _ in range(players-2)] + [str(SB_chips),str(BB_chips)]  # initial betting pot
'''Note: Can easily hard code the SB & BB chips to the end of the list as they will always
         be at the end of the list, by nature, since I have rotated UTG to be first.'''

# function which decides if betting has finished:
def bets_settled(lst=betting):
    settled = [False for _ in range(len(lst))]
    is_betting_over = True                # bettig is over until proven otherwise
    for k in range(len(lst)):
        if lst[k] == maximum(lst):        # if k == max
            settled[k] = True
        if lst[k].find('f') > -1:         # if 'f' does appear in k, ie. player has folded
            settled[k] = True
    if any(z == False for z in settled):  # someones not settled
        is_betting_over = False
    return is_betting_over                # TRUE if betting is over

# last player standing - folds function
def last_player_standing(lst=betting):
    end = False
    folded = [False for _ in range(len(lst))]
    for k in range(len(lst)):
        if lst[k].find('f') > -1:  # player folded
            folded[k] = True  
        if folded.count(False) == 1:  # if 'False' only appears once in the list
            end = True
            global winner_index
            winner_index = folded.index(False)
            global winner_name
            winner_name = temp_player_info['name'][folded.index(False)]
            global winner_chips
            winner_chips = temp_player_info['chips'][folded.index(False)]
            break

    return end


def betting_round(betting=betting):
    global Pot  # calling global variable to be used inside the function's scope
    first_run_done = False  # this variable allows the while loop to begin,
                              # so it doesnt get stuck on betting = [0,0,0]
    if last_player_standing() == True:
        print( winner_name,"Wins")
    else:
        while bets_settled() == False or first_run_done == False:
            # while any items != max(betting)  or  != 'f' somewhere in the string
            # while there is an item that is not 'f' or maximum(betting)
            if last_player_standing == True:
                break    # breaks out of this while loop after a fold occurs in the betting round.
            else:
                for j in range(players):
                    if bets_settled() == True and first_run_done == True:
                        # first_run_done = True shows everyone must have checked.
                        break  # breaks out of the for loop
                    elif 'f' in betting[j]:
                        print("player", temp_player_info['name'][j], "has folded")
                    elif any(i.isnumeric() and int(i)>0 for i in betting):  # if i != 'f' and >0 (bet placed)
                        # ie. if anything in the list is not '0' or 'f'
                        decision = input(temp_player_info['name'][j] + ", Enter " + str(int(maximum(betting)) - int(betting[j]))
                                           + " to call, 'f' to fold or enter an amount to raise: ")
                        if decision.isnumeric() == True:  # if decision is numeric <-could be decimal -> bug?
                            betting[j] = str(int(betting[j]) + int(decision))
                                      # v. confusing way of doing item + input ie. 0 + 50
                        elif decision == 'f':
                            betting[j] = betting[j] + decision  # concatenating 'f' onto the end
                        else:
                            print("typo? try again")
                            # need to re-iterate for value of j here
                    else:  # option to check
                        betting[j] = input(temp_player_info['name'][j] + ", Enter 0 to check, 'f' to fold or enter an amount to raise: ")
                first_run_done = True

    '''
    Improvments needed for betting loop function:
    1. if decision < maximum(betting) or decision != 'f':  # ie. input error. (or if any other input is entered for that matter)
    2. for BB, console displays: Enter 0 to call. Should be enter 0 to check.
    3. maybe a pause before the table_cards are turned over.
    '''
    
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

    if last_player_standing() == True:  # check for winner at the end too!
        print('\n     ',winner_name,"Wins", Pot, "chips")

        # give pot to winner:        
        temp_player_info['chips'][winner_index] += Pot
        Pot = 0  # resetting pot

        
    
    return print("\n players chip stacks:", temp_player_info['name'], temp_player_info['chips'], 'Pot =',Pot)

betting_round()  # first betting round
###########################################################################################################

''' CONSOLE DISPLAY ALTERNATIVE:
Could do something like...
for i in range(players):
    print('player',temp_player_info['name'][i]+"'s total chip stack is looking like:", temp_player_info['chips'][i])
'''

if last_player_standing() == False:
    # FLOP:
    table_cards = {}                              # creating a dictionary for table cards.
    table_cards['flop'] = cards_to_be_split[-3:]  # last 3 cards in the list will be the flop cards.
                                                  # They are moved to the table variable (ie. turned over)
    cards_to_be_split = cards_to_be_split[:-3]    # removing the flop cards from this list. 

    print("The flop is: ", table_cards['flop'],'\n')

    ## Betting Round for Flop:
    '''
    Altercations Needed: folded players need taking out/ set betting[folded players] = 'f'
    '''
    for o in range(players):
        if 'f' in betting[o]:  # player folded
            betting[o] = '0f'  # still folded in this round -> should skip this player
        elif betting[o].isnumeric():    # isnumeric = True if o doesnt contain 'f'
            betting[o] = '0'   # resetting betting

    betting_round()


# TURN
if last_player_standing() == False: 
    table_cards['turn'] = cards_to_be_split[-1:]  # last 3 cards in the list will be the flop cards.
                                                  # They are moved to the table variable (ie. turned over)
    cards_to_be_split = cards_to_be_split[:-1]    # removing the flop cards from this list. 
    print("The turn card is: ", table_cards['turn'], '\n')

    ## Betting Round for Turn:
    for o in range(players):
        if 'f' in betting[o]:  # player folded
            betting[o] = '0f'  # still folded in this round -> should skip this player
        elif betting[o].isnumeric():    # isnumeric = True if o doesnt contain 'f'
            betting[o] = '0'   # resetting betting

    betting_round()



# RIVER
if last_player_standing() == False: 
    table_cards['river'] = cards_to_be_split[-1:]  # last 3 cards in the list will be the flop cards.
                                                  # They are moved to the table variable (ie. turned over)
    cards_to_be_split = cards_to_be_split[:-1]    # removing the flop cards from this list. 
    print("The river card is: ", table_cards['river'], '\n')

    ## Betting Round for River:
    for o in range(players):
        if 'f' in betting[o]:  # player folded
            betting[o] = '0f'  # still folded in this round -> should skip this player
        elif betting[o].isnumeric():    # isnumeric = True if o doesnt contain 'f'
            betting[o] = '0'   # resetting betting

    betting_round()








# Showdown decision - who wins?

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



''' who_wins() function

0. create an empty list: showdown_winner = []  # name of winner
   create an empty list: showdown_hand = []    # hand strength = 10 for royal flush, 9 for straight flush, ..., 10 for high card

1. create dictionary: player_hands = {}
for i in range(players):
    player_hands[ temp_player_info['name'][i] ] = temp_player_info[hand][i] + table_cards  # player_hands['jeff'] = [11H, 11D, table_cards]

2. if last_player_standing() == False:  # showdown needed

    # 3. Royal flush?
    if 14,13,12,11,10 in player_hands['card_numbers']["matt's_hand"] and flush(player_hands['card_suits']["matt's_hand"]) == True:
        # Royal Flush potential - create new temp list with only cards that contain the highest cards: 10,11,12,13,14
        # Note that it doesnt matter if this list is 6 long, as when we check for flush - it either is a flush or it isnt.
        royal_flush_potential = indices(
        
        


        
    # 4. does player_hands['matt's_hand'] contain consecutive card_numbers?
    if player_hands['jeff's_hand'] contains 14,13,12,11,10:
        add these 5 cards to new list: royal_flush_potential
        Can be royal flush.. carry on     



    # 5. are all cards the same suit?
    if all(s == 'H' for s in royal_flush_potential['suit']) or all(s == 'D' for s in royal_flush_potential['suit']) ..... or ... spades or clubs
            showdown_winner.append(temp_player_info['name'][i])  # add this guy to winner list
            showdown_hand.append(10)  # add the hand strength = 10 for royal flush  

'''



# has player folded?
def player_folded(player_index, lst = betting, string = 'f'):
    if string in lst[player_index]:
        # player has folded
        return True
    else:
        # player has not folded
        return False

def card_number(string):  # gets the (integer) number of a single card
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)


        
# 1.
def arrange_hands2():  # this function creates a nice dictionary with the players (in the showdown) hands + table cards.
    global player_hands2                                                                                 
    player_hands2 = {}
    simplified_table_cards = []
    
    for card in range(len(table_cards_list)):  # card = 0, 1, 2, 3, 4  -> 5 table card index's
        if table_cards_list[card][1] == ' ':
            # single digit number
            simplified_table_cards.append(table_cards_list[card][0:3])

        if table_cards_list[card][1].isnumeric() == True:
            # double digit number
            simplified_table_cards.append(table_cards_list[card][0:4])

    # adding player hands - only if player has NOT folded
    for name in temp_player_info['name']:
        if player_folded(temp_player_info['name'].index(name)) == False:  # dont include folded players
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
            player_hands2["%s's_hand" % name] = {}  
            player_hands2["%s's_hand" % name]['cards'] = []  # creating a new list for each players sub-dic
            player_hands2["%s's_hand" % name]['cards'].append(first_card)  # adding each players card numbers
            player_hands2["%s's_hand" % name]['cards'].append(second_card)
            player_hands2["%s's_hand" % name]['cards'] += simplified_table_cards  # adding table cards

            # sorting the cards into ascending order
            player_hands2["%s's_hand" % name]['cards'] = sorted(player_hands2["%s's_hand" % name]['cards'], key = card_number)
            
            
    return player_hands2

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

# 2.
if last_player_standing() == False:   # showdown baby
    print("\n Its showdown time baby")

    # 1. 
    ## Creating player_hands list:
    # Need to add table_cards to each hand in the list
    table_cards_list = table_cards['flop'] + table_cards['turn'] + table_cards['river']
    print(table_cards_list)


    arrange_hands2()
    print('nicely arranged showdown hands: \n',player_hands2)


    

    def list_of_suits(lst):  # gets a list of suits from a list of cards
        suits = []
        for card in lst:
            suit = card[-1]  # last letter in the string (ie. the suit)
            suits.append(suit)
        return suits
            
    player_hands2["matt's_hand"]['cards'] = ['2 S', '7 D', '10 C', '11 C', '12 C', '13 C', '14 C']
    player_hands2["fox's_hand"]['cards'] = ['6 S', '7 S', '8 S', '9 S', '10 S', '13 H', '14 H']
    #player_hands2["jeff's_hand"]['cards'] = ['6 D', '7 C', '8 S', '9 S', '10 H', '12 S', '14 H']
    
    # 3. Royal Flush?
    # add this to 'arrange_hads()' function    
    ##### player_hands2["matt's_hand"] = ['10 H', '11 C', '11 H', '12 C', '12 H', '13 H', '14 H']
    print(player_hands2["matt's_hand"])
    def RoyalFlush():
        for name in player_hands2:
            royal_straight = []
            player_hands2[name]['handStr'] = []
            if 10 and 11 and 12 and 13 and 14 in card_number_list(player_hands2[name]['cards']):  # player has top straight
                high_card_indices = indices(card_number_list(player_hands2[name]['cards']), 14) + \
                                    indices(card_number_list(player_hands2[name]['cards']), 13) + \
                                    indices(card_number_list(player_hands2[name]['cards']), 12) + \
                                    indices(card_number_list(player_hands2[name]['cards']), 11) + \
                                    indices(card_number_list(player_hands2[name]['cards']), 10)
                for i in high_card_indices:
                    royal_straight.append(player_hands2[name]['cards'][i])  
                print(royal_straight)

                # is there a flush in the royal_straight?
                if len(indices(list_of_suits(royal_straight),'C')) >= 5 or \
                    len(indices(list_of_suits(royal_straight),'H')) >= 5 or \
                    len(indices(list_of_suits(royal_straight),'D')) >= 5 or \
                    len(indices(list_of_suits(royal_straight),'S')) >= 5:  # if there are 5+ cards of the same suit
                    print(name, 'got a Royal Flush Baby!!!')
                    Royal_Flush = True
                    # can index this list searching for 'True'. The index 0 will show Royal Flush,
                    # index 1 = straight Flush..... index 10 = High Card
                    # then player_hands2["%s's_hand" % names]['handStr'].index('True') will return the
                    # first handStr index that is True... ie. the players best hand.
                else:
                    print(name, 'didnt hit the royal flush.')
                    Royal_Flush = False
            else:
                print(name, 'didnt hit the royal flush.')
                Royal_Flush = False
            player_hands2[name]['handStr'].append(Royal_Flush)
        return 

    
    RoyalFlush()





    # 2. Straight Flush?
    '''
    straight_index is a list of all the card numbers that are consecutive eg. [3,4,5,11,12] - rename to 'consecutive'
    straight_indecies is a list of indecies needed to pull from 'player_hands2[name]['cards']
    straight_cards is the actual cards that are a straight, from which i can pull the suits from to check for straight flush.
    '''
    def StraightFlush():
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
            Straight = False
            for n in range(len(straight_index)):
                rotate(straight_index,n)  # rotating through the list so every element gets a change to be index 0.
                if straight_index[1] - straight_index[0] == 1 and \
                   straight_index[2] - straight_index[0] == 2 and \
                   straight_index[3] - straight_index[0] == 3 and \
                   straight_index[4] - straight_index[0] == 4:  # 5 consecutive cards
                    print(name, "hit a straight!")
                    # remove all other cards apart from 1st 5:
                    straight_index = straight_index[:5]  # 1st 5 cards
                    Straight = True
                    break
            if Straight == False:
                Straight_Flush = False  # by convention (no straight = no straight flush)
                print(name, "does not contain a straight(Flush)")
                return player_hands2[name]['handStr'].append(Straight_Flush)

            #if we still going in dis loop, Straight ==== True !!!
            # for each item in straight_index, get indecies refering to player_hands2[name]['cards']
            straight_indices = []
            for card in straight_index:  # gets indices relating to the cards in the straight
                straight_indices += indices(card_number_list(player_hands2[name]['cards']), card)
            # get cards(strings) of these indices:
            straight_cards = []
            for index in straight_indices:
                straight_cards.append(player_hands2[name]['cards'][index])
            
            # Flush?
            if len(indices(list_of_suits(straight_cards),'C')) >= 5 or \
               len(indices(list_of_suits(straight_cards),'H')) >= 5 or \
               len(indices(list_of_suits(straight_cards),'D')) >= 5 or \
               len(indices(list_of_suits(straight_cards),'S')) >= 5:  # if there are 5+ cards of the same suit
                # can always add 'if player didnt get royal flush: print(StraightFlush BABY!)'
                print(name, 'got a Straight Flush Baby!!!')
                Straight_Flush = True
            else:
                print(name, 'didnt hit the straight flush... but did hit the straight!')
                Straight_Flush = False
            player_hands2[name]['handStr'].append(Straight_Flush)
        return 



    StraightFlush()       
    print(player_hands2)
    













