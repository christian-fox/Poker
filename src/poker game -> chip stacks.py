######## poker game #########
"""
 pseudo code
 Steps:
 1. creating a deck of cards
 2. choose number of players (up to 8)
 3. blinds
 4. dealing process - deal 2 random cards to each player
 5. assign chips - pot - and players stack
 6. preflop betting 
 7. flop 
     8. betting              <
     9. turn                 <
     10. betting             < copy paste job
     11. river               < 
     12. final betting       <
 13. deciding who wins - give them pot - update chip stacks (save)
 14.  deal new hand

 << possible situations/problems >>
 second pot. - possibly 3rd pot
 everyone folds
 elimination button/blinds protocol

 << xtras >>
 timer for blinds
 ante
 bomb pot
 straddle
 cash game
"""

# RULES
print("RULES:\n"
      "1. This is a 2-8 player game. There is technically no upper limit this game could do but "
      "irl poker tables have max of 8.\n"
      "2. This game will require patience as it is inevitable to break. Thanks.\n"
      "3. No whining when Fox takes all your money :)\n")


################################# EVERYTHING CARD RELATED ####################################
# Creating a deck of cards (w/o 'class')
number = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]  # list of card numbers
suit = ["Hearts", "Diamonds", "Spades", "Clubs"]

# this loop changes the data type of all elements of the list to string.
object_number = 0
for num in number:
    if type(num) != "<class 'str'>":  # (conditional not actually needed here)
        number[object_number] = str(num)
        object_number += 1

# matching number to suit (ie. generating the 52 cards)
deck = []
for i in suit:
    for j in number:
        card = j + " of " + i
        deck.append(card)  # adds the specific 'card' to the list 'deck'


"""
# Creating a card deck with 'class'
class Deck:

    number = list(range(2,11)) + ["Jack", "Queen", "King", "Ace"];  # list of card numbers
    
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.card = number + " of " + suit




# A_Card = Deck('4','hearts')
# print(A_Card.card)
"""


# having a look at 'random' library :
'''
choice() - Returns a random element from the given sequence
randint() / randrange() - Returns a random number between the given range

Things to keep in mind:
seed() - Initialize the random number generator
getstate() - Returns the current internal state of the random number generator
shuffle() - Takes a sequence and returns the sequence in a random order
'''
import random

# closer look at a potential dealing bug: (commented out)
'''
print(random.choice(deck),'/', random.choice(deck)) # <- could be dealt the same 2 cards

# showing this method could deal 2 identical cards:
card1 = random.choice(deck)
card2 = random.choice(deck)
iterations = 0
while card1 != card2:
    iterations += 1
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    if card1 == card2:
        print("Card 1 =",card1, " and Card 2 =",card2, ". They are the same!")
        break
print("This took",iterations,"deals")


# odds of this bug happening:
matches = 0
for iteration in range(1,1000000):
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    if card1 == card2:
        matches +=1
print("There were",matches, "in 1 million deals, giving the odds of this bug happening as", 100*matches/1000000)
print("This number is the same as 1/52 (=0.0192)")

These tests have given the IDEA to test the dealt hands to make sure every combination (for each hand) arises equally.
'''


# could always add more shuffling in the card assignment process.. would this increase the randomness of the process?

# Dealing to 2 separate players:
Players = int(input("Enter number of players: "))



cards_to_be_split = random.sample(deck, k = 2*Players + 5)  # produces a list of [2*Players] cards to be dealt to the players.
                                                        # random.sample() takes a random list from the deck of cards,
                                                        # and the arg. k is the size of the list.
                                                        # The [+5] here are the 'table' cards, and will be turned over later.

# IDEA: loop over (*players*) variables (ie. if players=3, then create 3 new variables)
    #  then use list splitting to take the last 2 cards from the list and put onto hand1.. repeat for all players.
    #  the 2 concepts here are: 1. creating a variable amount of variables and 2. list manipulation

# creating the hands:
'''
Description: Creates x new variables (where x is the number of players) and splits the list of cards
 into x pairs of cards and assigns each pair of cards to each variable.
 Now left with a dictionary of variables named hand1, hand2,...,handx, all of which have a list of 2
 random cards from the deck assigned to them.
'''
all_hands = {}   # creates a dictionary of variables
Player = {}  # dic for chip stacks
Player['chips'] = [1000 for _ in range(Players)]  # creates a list of size: Players, with all elements = 1000
for i in range(1, Players+1):  # if 3 players -> i=1,2,3.
    var_name = "hand%d" % i    # this creates i variables, called hand1, hand2, hand3...
                               # the %d represents an integer. %s represents a string.
    all_hands[var_name] = cards_to_be_split[-2:]  # assigns the last 2 cards on the list to hand1.
    cards_to_be_split = cards_to_be_split[:-2]    # removes these 2 last cards from the original list.

    var_name2 = "Player%d_chips" % i              # chip stacks -> Player1_chips
    Player['chips'][i-1] = {var_name2: '1000'}     # Assigns a sub-dictionary to 'chips' with each players initial chip stack

print("Starting stacks shown: ", Player)
print('\n Here are the hands that have been dealt:\n ', all_hands, '\n')   # printing the dictionary of the hands
print("Showing I can select player2's 1st card: ", all_hands['hand2'][0])  # accessing a certain card in the dictionary
print("Current chip stacks: ", Player)

# FLOP
table_cards = {}  # creating a dictionary for table cards.
table_cards['flop'] = cards_to_be_split[-3:]  # last 3 cards in the list will be the flop cards.
                                              # They are moved to the table variable (ie. turned over)
cards_to_be_split = cards_to_be_split[:-3]    # removing the flop cards from this list.

# PRE-FLOP BETTING
  # -> First, assign SB, BB and UTG.
# Letting P1 be dealer to start
''' CHANGE THIS TO PROPER PRACTISE LATER'''



print("The flop is: ", table_cards['flop'])

# TURN
table_cards['turn'] = cards_to_be_split[-1:]  # last card in the list. <- could always choose the first card instead..
cards_to_be_split = cards_to_be_split[:-1]

print("The turn card presents itself: ", table_cards['turn'])

''' IDEA: create a dictionary of phrases that the dealer could say here - refer to the discord joke bot repository. '''

# RIVER
table_cards['river'] = cards_to_be_split[:]  # copy pasting flop & turn. see comments there.
cards_to_be_split = cards_to_be_split[:]     # There should be only 1 item left in this list so the inside
                                             #  of the sq. brackets can either have 0,:,-1:,...
print("The river card is: ", table_cards['river'])











################################## POT #######################################

# should i implement the pot now or implement the betting rounds? or folding?

























