''' POKER GAME'''

'''
Version 2.8:
Decifering between same hand strength:
if there are 2+ min(index(True)) for 'handStr', then decifer().
new func: decifer()



'''
# Defining initial variables:
players = 2#int(input("How many players? "))  # number of players




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
temporary = ['matt','fox']  # delete

# this loop obtains the players names and prints them.
for i in range(1, players+1):
    name = temporary[i-1]#input('Enter ' + 'Player' + str(i) + ' Name: ')
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
SB_chips = 20
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
                        decision = "0" '''input(temp_player_info['name'][j] + ", Enter " + str(int(maximum(betting)) - int(betting[j]))
                                           + " to call, 'f' to fold or enter an amount to raise: ")
                                        '''
                        if decision.isnumeric() == True:  # if decision is numeric <-could be decimal -> bug?
                            betting[j] = str(int(betting[j]) + int(decision))
                                      # v. confusing way of doing item + input ie. 0 + 50
                        elif decision == 'f':
                            betting[j] = betting[j] + decision  # concatenating 'f' onto the end
                        else:
                            print("typo? try again")
                            # need to re-iterate for value of j here
                    else:  # option to check
                        betting[j] = "0"#input(temp_player_info['name'][j] + ", Enter 0 to check, 'f' to fold or enter an amount to raise: ")
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
'''
could create a who_wins() function.. idk
'''

# function to find all occurences of an element in a list - {gives index of the occurance(s)}
def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

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
if last_player_standing() == False:   # showdown baby - if there are 2 or more players who havent folded - showdown
    print("\n Its showdown time baby")

    # 1. 
    ## Creating player_hands list:
    # Need to add table_cards to each hand in the list
    table_cards_list = table_cards['flop'] + table_cards['turn'] + table_cards['river']

    arrange_hands2()
    print('nicely arranged showdown hands: \n',player_hands2)


    

    def list_of_suits(lst):  # gets a list of suits from a list of cards
        suits = []
        for card in lst:
            suit = card[-1]  # last letter in the string (ie. the suit)
            suits.append(suit)
        return suits
          
    #player_hands2["matt's_hand"]['cards'] = ['3 S', '4 C', '5 S', '6 H', '6 D', '8 S', '13 S']
    player_hands2["fox's_hand"]['cards'] = ['2 S', '2 C', '4 C', '5 S', '8 H', '10 D', '13 S']
    player_hands2["matt's_hand"]['cards'] = ['2 S', '2 C', '4 C', '5 S', '8 H', '10 D', '13 S']
    
    
    # 3. Royal Flush?
    # add this to 'arrange_hads()' function    
    ##### player_hands2["matt's_hand"] = ['10 H', '11 C', '11 H', '12 C', '12 H', '13 H', '14 H']
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
                    #print(name, 'didnt hit the royal flush.')
                    Royal_Flush = False
            else:
                #print(name, 'didnt hit the royal flush.')
                Royal_Flush = False
            '''
            if Royal_Flush == True:
                SameHandStr_dic[name]['StraightFlush'] = ***RoyalFlush_cards***
            # adding top 5/7 cards as there is no flush
            '''
            player_hands2[name]['handStr'].append(Royal_Flush)
        return 

    
    RoyalFlush()


    # 2. Straight Flush?
    SameHandStr_dic = {}  # creating a storage space for deciding who has the better hand when SameHandStr = True.
    for name in player_hands2:
        SameHandStr_dic[name] = {}
    
    '''
    straight_index is a list of all the card numbers that are consecutive eg. [3,4,5,11,12] - rename to 'consecutive'
    straight_indecies is a list of indecies needed to pull from 'player_hands2[name]['cards']
    straight_cards is the actual cards that are a straight, from which i can pull the suits from to check for straight flush.
    '''
    def StraightFlush():
        # Straight?
        Straight = False  # until proven otherwise
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
                    if straight_dic[1][0] - straight_dic[key][0] == -12:  # no combination of cards other than 2 - 14 that could = -12
                        straight_index += [straight_dic[key][0]] + [straight_dic[1][0]]
                elif straight_dic[key][1] - straight_dic[key][0] == 1:
                    straight_index += [straight_dic[key][0]] + [straight_dic[key][1]]  # adds both numbers of tuple
            # remove duplicates from straight_index:
            straight_index = list(dict.fromkeys(straight_index))  # creates a dic key for each value then morphs back into a list of each unique key
                
            # 5 cards in a row?
            for n in range( len(straight_index)):  # start from 1 to rotate the lowest number 
                # bug: only a few consecutive cards:
                if len(straight_index) < 5:
                    break
                if len(straight_index) == 6:  # 6 cards in a row
                    n = 1  # make sure to rotate the lowest card to the end, then take the first 5 cards
                if len(straight_index) == 7:  # 7 cards in a row
                    n = 2  # these if statements just make sure the highest 5 out of 7 cards are chosen
                # ^^^ this makes sure straight_index will take only the 5 highest straight cards.
                straight_index = rotate(straight_index,n)  # rotating through the list so every element gets a change to be index 0.
                if straight_index[1] - straight_index[0] == 1 or straight_index[1] - straight_index[0] == -12:  # accomodating for ace at start
                    if straight_index[2] - straight_index[1] == 1 and \
                        straight_index[3] - straight_index[2] == 1 and \
                        straight_index[4] - straight_index[3] == 1:  # 5 consecutive cards
                        # remove all other cards apart from 1st 5:
                        straight_index = straight_index[:5]  # 1st 5 cards
                        Straight = True
                        break               

            #if we still going in dis loop, Straight ==== True !!!
            # for each item in straight_index, get indecies refering to player_hands2[name]['cards']
            straight_indices = []
            for card in straight_index:  # gets indices relating to the cards in the straight
                straight_indices += indices(card_number_list(player_hands2[name]['cards']), card)
            # get cards(strings) of these indices:
            global straight_cards
            straight_cards = []
            for index in straight_indices:
                straight_cards.append(player_hands2[name]['cards'][index])
            
            # Flush?
            Flush = False
            flush_cards = []  # setting storage for (potential) flush cards
            if len(indices(list_of_suits(player_hands2[name]['cards']),'C')) >= 5:
                #print(indices(list_of_suits(player_hands2[name]['cards']), 'C'))  - dont think i need
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'C'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                #print(name, 'hit a flush') - dont think i need
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'H')) >= 5:
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'H'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'D')) >= 5:
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'D'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'S')) >= 5:  # if there are 5+ cards of the same suit
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'S'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            # NOTE: let flush_cards list be >5 long ie. leave all flush cards in the list. - Do not take 5 highest.
                    
            
            if Straight == True and Flush == True:
                print(name, 'got a Straight Flush Baby!!!')
                Straight_Flush = True
                # obtaining StraightFlush cards:
                StraightFlush_cards = set(straight_cards).intersection(flush_cards)
                StraightFlush_cards = sorted(StraightFlush_cards, key = card_number)  # sort into ascending order
                print('3 cards?',StraightFlush_cards)
                # adding the cards to SameHandStr_dic
                SameHandStr_dic[name]['StraightFlush'] = StraightFlush_cards
            else:
                Straight_Flush = False
                #print(name, 'did not get a straight flush')
                SameHandStr_dic[name]['StraightFlush'] = []  # leaving empty
            player_hands2[name]['handStr'].append(Straight_Flush)
        return 



    StraightFlush()
    

    # 4 of a kind?
    '''
    1. use indices() to get a list of indices for each card number (using for loop)
    2. evaluate: if len(list) == 4: then you have 4 of a kind!
                 else: you dont have 4 of a kind.
    '''
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
                    print(type(quad_cards))
                    for index in indices(card_number_list(player_hands2[name]['cards']), num):
                        quad_cards.append(player_hands2[name]['cards'][index])
                        # need 1 more card added to the list - got the 4 cards for the 4 of a kind. need the next highest card.

            if four_of_a_kind == True:
                # adding the cards to SameHandStr_dic
                SameHandStr_dic[name]['Quads'] = quad_cards
            if four_of_a_kind == False:  
                SameHandStr_dic[name]['Quads'] = []  # leaving empty
            player_hands2[name]['handStr'].append(four_of_a_kind)
        return

    Quads()


    # Full House?
    '''
    1. use indices() to check for 3 of a kind as in the Quads() func.
    2. remove these from the list we are checking
    3. now re-run through all numbers and check for a pair.
    '''

    def Boat():
        for name in player_hands2:
            Full_House = False
            for num in range(2,15):  # num = 2,3,4,...,14
                ###Set = False
                if len(indices(card_number_list(player_hands2[name]['cards']), num)) == 3:
                    #print(name, "hit trips")
                    ###Set = True
                    # removing this 3 of a kind from the list:
                    pair_check = player_hands2[name]['cards'].copy()  # duplicating the list
                    boat_cards = []  # creating storage for (potential) boat cards (for if the boat hits)
                    for i in sorted(indices(card_number_list(player_hands2[name]['cards']), num), reverse=True):
                    # for index in list of indices which are part of the Set (in reverse order) so we can safely remove the last index first.
                        pair_check.pop(i)
                        boat_cards.append(player_hands2[name]['cards'][i])  
                    # pair_check is the new list with the 3 of a kind cards removed.
                    # now check for pair:
                    for num in range(2,15):
                        if len(indices(card_number_list(pair_check), num)) == 2:
                            print(name, "HIT THE BOAT!!!")
                            Full_House = True
                            # adding the cards to SameHandStr_dic
                            for i in sorted(indices(card_number_list(pair_check), num)): # no need to be reverse, as i am not using pop()
                                boat_cards.insert(0,pair_check[i])  # .insert adds to front (whereas .append adds to end)
                            print('BOAT CARDS:', boat_cards)
                            SameHandStr_dic[name]['Boat'] = boat_cards
            if Full_House == False:  
                SameHandStr_dic[name]['Boat'] = []  # leaving empty
            player_hands2[name]['handStr'].append(Full_House)
        return
    Boat()


    # Flush?
    def Flush():
        for name in player_hands2:
            Flush = False
            flush_cards = []  # setting storage for (potential) flush cards
            if len(indices(list_of_suits(player_hands2[name]['cards']),'C')) >= 5:
                #print(indices(list_of_suits(player_hands2[name]['cards']), 'C'))  - dont think i need
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'C'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                #print(name, 'hit a flush') - dont think i need
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'H')) >= 5:
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'H'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'D')) >= 5:
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'D'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            if len(indices(list_of_suits(player_hands2[name]['cards']),'S')) >= 5:  # if there are 5+ cards of the same suit
                for i in indices(list_of_suits(player_hands2[name]['cards']), 'S'):
                    flush_cards.append(player_hands2[name]['cards'][i])
                Flush = True
            if Flush == True:
                # adding the cards to SameHandStr_dic
                # only want top 5 flush cards:  # not essential, as it wont effect HighCard() 
                while len(flush_cards) > 5:
                    flush_cards.pop(0)  # removes 1st item from list
                SameHandStr_dic[name]['Flush'] = flush_cards  # storing flush hand

            if Flush == False:
                SameHandStr_dic[name]['Flush'] = []  # leaving empty
            player_hands2[name]['handStr'].append(Flush)
        return

    Flush()


    # Straight?
    def Straight():
        for name in player_hands2:
            Straight = False
            straight_dic = {1: (), 2: (), 3: (), 4: (), 5: (), 6: (), 0: ()}
            straight_index = []
            refined_straight_cards = []  # for removing duplicates(pairs) out of the final straight cards that will go into SameHandsStr_dic
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
                    if straight_dic[1][0] - straight_dic[key][0] == -12:  # no combination of cards other than 2 - 14 that could = -12
                        straight_index += [straight_dic[key][0]] + [straight_dic[1][0]]
                elif straight_dic[key][1] - straight_dic[key][0] == 1:
                    straight_index += [straight_dic[key][0]] + [straight_dic[key][1]]  # adds both numbers of tuple
            # remove duplicates from straight_index:
            straight_index = list(dict.fromkeys(straight_index))  # creates a dic key for each value then morphs back into a list of each unique key

            # 5 cards in a row?
            # ^^^ this makes sure straight_index will take only the 5 highest straight cards.
            for n in range(len(straight_index)):
                # bug: only a few consecutive cards:
                if len(straight_index) < 5:
                    break
                if len(straight_index) == 6:  # 6 cards in a row
                    n = 1
                if len(straight_index) == 7:  # 7 cards in a row
                    n = 2  # these if statements just make sure the highest 5 out of 7 cards are chosen
                straight_index = rotate(straight_index,n)  # rotating through the list so every element gets a change to be index 0.
                if straight_index[1] - straight_index[0] == 1 or straight_index[1] - straight_index[0] == -12:  # accomodating for ace at start
                    if straight_index[2] - straight_index[1] == 1 and \
                        straight_index[3] - straight_index[2] == 1 and \
                        straight_index[4] - straight_index[3] == 1:  # 5 consecutive cards
                        print(name, "hit a straight!")
                        # remove all other cards apart from 1st 5:
                        straight_index = straight_index[:5]  # 1st 5 cards
                        Straight = True
                        # for each item in straight_index, get indecies refering to player_hands2[name]['cards']
                        straight_indices = []
                        for card in straight_index:  # gets indices relating to the cards in the straight
                            straight_indices += indices(card_number_list(player_hands2[name]['cards']), card)
                        # get cards(strings) of these indices:
                        straight_cards = []
                        for index in straight_indices:
                            straight_cards.append(player_hands2[name]['cards'][index])
                            # removing duplicate card numbers from the straight_cards list (so there will only be 5 cards in the list)
                            for x in straight_cards:
                                if card_number(x) not in card_number_list(refined_straight_cards):
                                    refined_straight_cards.append(x)
                        break
                
            #print(name, "does not contain a straight")
            SameHandStr_dic[name]['Straight'] = refined_straight_cards  # adds either an empty list when straight = False, or the actual cards when it is true.
            player_hands2[name]['handStr'].append(Straight)
        return


    Straight()


    '''
    finish 3 of a kind, 2 pair, pair and high card
    then try to make straight flush and royal flush more efficient by defining straight and flush before
    and just calling Straight() and Flush() {nested inside the functions}

     and define pair() funcion from boat()   

    '''


    # 3 of a kind?
    def Set():
        for name in player_hands2:
            Set = False
            for num in range(2,15):  # num = 2,3,4,...,14
                if len(indices(card_number_list(player_hands2[name]['cards']), num)) == 3:  # if there are 3 cards of the same number
                    print(name, "hit trips")
                    Set = True
                    # adding set_cards (best 5) to SameHandStr_dic:
                    remaining_2_cards_index = list({0,1,2,3,4,5,6} - set(indices(card_number_list(player_hands2[name]['cards']), num)))[-2:]  # max 2 indicies that is not already an index of one of the quad cards
                    set_cards = [player_hands2[name]['cards'][remaining_2_cards_index[0]],player_hands2[name]['cards'][remaining_2_cards_index[1]]]  # 2 highest cards
                    for index in indices(card_number_list(player_hands2[name]['cards']), num):
                        set_cards.append(player_hands2[name]['cards'][index])
                    SameHandStr_dic[name]['Set'] = set_cards
            if Set == False:
                SameHandStr_dic[name]['Set'] = []  # leaving empty
            player_hands2[name]['handStr'].append(Set)
        return
    print(player_hands2)
    Set()
    




    # 2 pair?
    def TwoPair():
        for name in player_hands2:
            Two_Pair = False
            for num in range(2,15):  # num = 2,3,4,...,14
                if len(indices(card_number_list(player_hands2[name]['cards']), num)) == 2:
                    #print(name, "hit 1 pair")
                    
                    # removing this pair from the list:
                    second_pair_check = player_hands2[name]['cards'].copy()  # duplicating the list
                    for i in sorted(indices(card_number_list(player_hands2[name]['cards']), num), reverse=True):  # the indicies of the first pair
                    # for index in list of indices which are part of the Set (in reverse order) so we can safely remove the last index first. - doesnt mix up index numbers/positions
                        second_pair_check.pop(i)
                    # now check for second pair:
                    for num2 in range(2,15):
                        if len(indices(card_number_list(second_pair_check), num2)) == 2:
                            print(name, "Hit 2 pair")  # if 3 pairs, this prints twice lol ----- fix(or just dont print this stuff - only print best hand.
                            Two_Pair = True
                            # obtaining TwoPair_cards for SameHandStr_dic
                            print(player_hands2[name]['cards'], card_number_list(second_pair_check))
                            TwoPair_indices = indices(card_number_list(player_hands2[name]['cards']), num) + indices(card_number_list(second_pair_check), num2)
                            print('TwoPair_indices = ', TwoPair_indices)
                            # relating indices to actual cards:
                            TwoPair_cards = [player_hands2[name]['cards'][c] for c in TwoPair_indices]
                            # sort the two pairs in order - (lowest pair as index 0,1 and highest pair at index 2,3)
                            TwoPair_cards = sorted(TwoPair_cards, key = card_number)
                            # removing the two pair cards from the players 7-card hand then taking the last card in the list - the max card number
                            last_card = sorted(set(player_hands2[name]['cards']) - set(TwoPair_cards), key = card_number)[-1]               
                            TwoPair_cards.insert(0,last_card)  # adding final card to the beginning of the list - setting up for decipher stage
                            # adding TwoPair_cards to SameHandStr_dic
                            SameHandStr_dic[name]['TwoPair'] = TwoPair_cards

            if Two_Pair == False:  
                SameHandStr_dic[name]['TwoPair'] = []  # leaving empty
            player_hands2[name]['handStr'].append(Two_Pair)
        return
    

    TwoPair()
    

    # Pair?
    def Pair():
        for name in player_hands2:
            Pair = False
            for num in range(2,15):  # num = 2,3,4,...,14
                if len(indices(card_number_list(player_hands2[name]['cards']), num)) == 2:
                    if player_hands2[name]['handStr'][7] == False:  # no two-pair
                        print(name, "hit 1 pair")
                        Pair = True
                        # adding pair_cards (best 5) to SameHandStr_dic:
                        remaining_3_cards_index = list({0,1,2,3,4,5,6} - set(indices(card_number_list(player_hands2[name]['cards']), num)))[-3:]  # max 3 indicies that is not already an index of one of the quad cards
                        pair_cards = [player_hands2[name]['cards'][remaining_3_cards_index[0]],player_hands2[name]['cards'][remaining_3_cards_index[1]], player_hands2[name]['cards'][remaining_3_cards_index[2]]]  # 2 highest cards
                        for index in indices(card_number_list(player_hands2[name]['cards']), num):
                            pair_cards.append(player_hands2[name]['cards'][index])   
                        SameHandStr_dic[name]['Pair'] = pair_cards
            if Set == False:
                SameHandStr_dic[name]['Pair'] = []  # leaving empty
                        
            player_hands2[name]['handStr'].append(Pair)
        return

    Pair()



    
    # High Card
    for name in player_hands2:  # this sets ['best_cards'] key to 5 highest cards
        five_best_cards = sorted(card_number_list(player_hands2[name]['cards'][-5:]),reverse = True)  # last(highest) 5 cards, in reverse
        player_hands2[name]['high_card'] = five_best_cards
    '''
    can use the HighCard() function in the decifer function to decifer between same handStr..
    however, need to change the ['handStr'] key in player_hands2 dic.
    '''

    def HighCard():# make sure to change player_hands2[name]['high_card'] list if i want to use this func for other things.
        high_card_player = [name for name in player_hands2]  # player list
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
            

        
        
        for name in player_hands2:  # adding the high card player to each players 'handStr' key.
            player_hands2[name]['handStr'].append('')
            player_hands2[name]['handStr'][-1] = high_card_player[:]  # add the list, in case there is 2+ players
        return high_card_player

    HighCard()
    #print(player_hands2)

    
    

        


    ############################################################################
    # Decifer()
    '''
    player_hands2 = {"b's_hand": {'cards': ['2 S', '2 H', '2 C', '3 D', '7 C', '8 D', '12 D'],
                                  'handStr': [False, False, False, False, False, False, True, False, False, ["a's_hand"]],
                                  'high_card': [12, 8, 7, 3, 2]},
                     "a's_hand": {'cards': ['2 H', '2 C', '3 D', '4 H', '8 C', '8 D', '12 D'],
                                  'handStr': [False, False, False, False, False, False, True, False, False, ["a's_hand"]],
                                  'high_card': [12, 8, 8, 4, 3]}}
    '''
    print('\n', SameHandStr_dic)
    # Each players best hand:
    best_hand = {}
    high_card = []
    for name in player_hands2:  # getting a list of handStr index - morph handStr key's.
        best_hand[name] = []
        try:
            best_hand[name] = player_hands2[name]['handStr'].index(True)  # the index of each players best hand
        except ValueError:  # ValueError because of the last HighCard() adds a list of names to the 'handStr' key
            best_hand[name] = 9  # 9 is for high_card

    # created best_hand2 for the display console
    best_hand2 = {}
    for k,v in best_hand.copy().items():  # k = name, v = hand_number
        best_hand2[k] = list(SameHandStr_dic[k].keys())[v-1]
        
    
    print('\n',best_hand2,'\n')
        
    if any(v < 9 for k,v in best_hand.items()) == True:  # need a route for equal high cards!!!!! - if 2 players got 9, then split pot.
        #print('we got a hand better than high_card')
        best_hand_index = min(best_hand.values())  # best hand index
        for k,v in best_hand.items():  #''' guessing this runs through 1st k then all v for that k then next k ...'''
            if v != best_hand_index:  # if the players best hand != best hand index
                player_hands2.pop(k, None)  # delete the players who dont make the cut from player_hands2
            if len(player_hands2) == 1:
                print('winner:,', [key for key in player_hands2.keys()][0])  # <- how to print the first key in the dict
                break  # is this needed?
    else:
        print('all False (ie. not even a single pair)')
        print('winner(s): ', player_hands2[name]['handStr'][-1])  # players winning by HighCard().
    


    ############################################################################################
    # if no-one has won yet..
    ############################################################################################
    ''' ASSUMING NOBODY HAS WON YET AFTER THIS POINT - >1 PLAYER HAS THE CURRENT BEST HAND - CAN USE INDEX 0 FROM SameHandStr_dic'''


    def Best_hand():  # Rename to best_hand() - works not only for straight flush, but for every handStr
                                                    # - .. as it takes index 0 of the dic which is the current best hand            
        # create a highCard() function - running through card indices 4 -> 0
                #for hand_name,card_list in sub_dic.items():
                    #print(hand_name,card_list)
        HighCard = []
        for name,sub_dic in SameHandStr_dic.items():
            for hand_name,card_list in sub_dic.items():
                if card_list != []:  # this could be taken out the loop for better runtime/efficiency
                    break
            HighCard.append(card_list)
             
        for x in range(4,-1,-1):  # x = 4,3,2,1,0               [below vvvvvvvvv is the names in the dic] [card_number_list as we are not interested in suits]
            HighCard_compare = card_number_list([HighCard[y][x] for y in range(len(list(SameHandStr_dic.keys())))])  # takes cards from each player starting from each players last card in SameHandStr_dic
            #winner_index = HighCard_compare.index(max(HighCard_compare))
            winner_index = [index for index, value in enumerate(HighCard_compare) if value == max(HighCard_compare)]
            #if isinstance(winner_index, int) == True: # winner found - max() function not returned >1 index - dont know why if type(winner_index) doesnt work?
            if len(winner_index) == 1:  # above line obsolete as winner_index is re-defined as always being a list.
                print(list(SameHandStr_dic.keys())[winner_index[0]], 'has the best', hand_name, 'and therefore wins!')
                temp_player_info['chips'][winner_index[0]] += int(Pot)  # are names in temp_player_info in same order as in SameHandStr_dic? - dont see why not
                print(temp_player_info)
                break

        #if isinstance(winner_index, int) == False:  # still not got one winner
        if len(winner_index) >= 2:
            # split pot between whoever had best hand
            print('split pot between', list(SameHandStr_dic.keys()))
            print(temp_player_info)
            for player in range(len(list(SameHandStr_dic.keys()))):
                print(player)
                temp_player_info['chips'][player] += int(Pot/len(list(SameHandStr_dic.keys())))  # Pot/ amount of players

        print('here are all the hands containing a', hand_name)  # cant find backslash for newline command
        for names in SameHandStr_dic:
            print(names, SameHandStr_dic[names][hand_name])
        print(temp_player_info)

        return
    
    Best_hand()
        

    print("!!!!!!!!!!!!!!!!!!!!! same hands str dic!!!!!!!!!!!!!!!!\n", SameHandStr_dic)
    # would the flush key in this dic be enough??? - why dont i just take high card from straightflush list?
    #                                              - why isnt straightflush list working properly? - not a big deal (i dont think)
    # why is this dictionary listing all hands and not just the best hand? - only need straight flush hand, not the rest.
    #                                                                      - then perform HighCard() on both besthands.
    # ^ the above happens because SameHandStr_dic is added to during each function - StraightFlush(), Flush(), Straight()...
    # have we already decifered >1 player with best hand and seperated these players?
    #                                             - if so, just take key index 0 (first/best hand in the dic) and do high_card() on it.





    '''
    end of 1/5/21

    created code for the better straight flush - specific case.
    check to make sure the list 'high_card_player' has already ciphened out all players with worse hands. **DONE**
    run code where fox and matt both have equal straight flushes.  **DONE**
    test whether BestStraightFlush() works on all hands - ie. for the Best Pair..  ****
        -> make sure each hand has their best 5 cards added to the 'SameHandStr_dic'


    '''


'''
1/5/21: Looking back, it looks like i have used too many functions where they are not needed. eg. BestStraightFlush()
'''























