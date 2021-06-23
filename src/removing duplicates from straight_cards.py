# Removing duplicates from straight cards

def card_number(string):  # gets the (integer) number of a single card
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)

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



straight_cards =  ['6 D', '7 C', '8 S', '8 D', '9 S', '10 H', '10 S']

output = []
for x in straight_cards:
    if card_number(x) not in card_number_list(output):
        output.append(x)
print(output)




