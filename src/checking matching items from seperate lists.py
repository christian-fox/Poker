# matching items in 2 lists.

def card_number(string):  # gets the (integer) number of a single card
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)




straight_cards = ['3 H', '4 H', '4 D', '5 H', '6 H', '7 H']
flush_cards = ['3 H', '5 H', '6 H', '7 H', '13 H', '4 H']

StraightFlush_cards = set(straight_cards).intersection(flush_cards)
print(StraightFlush_cards)

StraightFlush_cards = sorted(StraightFlush_cards, key = card_number)
print(StraightFlush_cards)















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

print(max(card_number_list(flush_cards)))

