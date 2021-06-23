''' POKER GAME'''
# Defining initial variables:
players = int(input("How many players? "))  # number of players




# Creating a deck of cards.
number = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]  # list of card numbers
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]

## this loop changes the data type of all elements of the list to string.
object_number = 0
for num in number:
    if type(num) != "<class 'str'>":  # (conditional not actually needed here)
        number[object_number] = str(num)
        object_number += 1

## matching number to suit (ie. generating the 52 cards)
deck = []
for i in suit:
    for j in number:
        card = j + " of " + i
        deck.append(card)  # adds the specific 'card' to the list 'deck'


## Dealing.
import random
'''
 (this line below) Produces a list of [2*Players] cards to be dealt to the players.
 random.sample() takes a random list from the deck of cards,
 and the arg. k is the size of the list.
 The [+5] here are the 'table' cards, and will be turned over later.
'''
cards_to_be_split = random.sample(deck, k = 2*players + 5)
print(cards_to_be_split)


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


'''
NEXT TASK's
assign dealer, small blind, bb, utg

'''

# Assigning dealer:
'''
quick fix: if there are 2 high cards, then just regenerate the high_card list.
proper fix: if there are 2 high cards, then do an other round with just these people involved.
'''
## adding a 'hand' key to player info dictionary:
high_card = random.sample(deck,k=players)
player_info['hand'] = high_card
print(player_info)

## getting positions of largest elements in high_card list
print(high_card.index(max(high_card)))  # list of the positions where the highest card shows up in 'high_card' list

# not working because the items in high_card list are strings


# need to go back to the numbers and create another list of numbers in integer format
# then at the end, before printing the dictionaries (player_info['hand']) and table_cards,
# just change 11,12,13,14 to jack,queen,king,ace.

print(type(high_card[0]))


































