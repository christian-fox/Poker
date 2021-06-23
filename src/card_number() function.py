def card_number(lst,index):
    #for i in range(len(lst)):
    if lst[index][1].isnumeric() == True:
        # double digit number
        number = lst[index][0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = lst[index][0]
    return int(number)


def card_numbers(lst):  # gives the card number (as an integer)
    number_list = []
    card_list = [0 for _ in range(len(lst))]
    for i in range(len(lst)):
        if lst[i][1].isnumeric() == True:
            # double digit number
            number = int(lst[i][0:2])
            number_suit = lst[i][3]
            number_list.append(number)
        else:  #if lst[i][1] == ' ':
            # single digit number
            number = int(lst[i][0])
            number_suit = lst[i][2]
            number_list.append(number)
        # ^ added number to number_list ^
        #number_list.sort()  # sort number list
    print(number_list)
    return number_list

'''    
    # loop which aims to re-add suit to cards
    for k in range(len(number_list)):  # k = 0 -> 6
        print('k=',k)
        if number_list[k] == lst[k] and type(card_list[k]) != "<class 'str'>":
            # think this is same as 'number' variable
            # right number, make sure it has not had a suit already assigned
            print('IM REPLACING!!!')
            card_list[k] = lst[k]
            print('card_list=',card_list)
            break
                
        
        
    return print(number_list, card_list)

'''

fox_hand = ['11 D', '14 C', '2 S', '3 S', '4 D', '8 C', '9 C']

matt_hand = ['10 D', '11 D', '14 C', '2 S', '3 S', '5 C', '8 C']


#card_numbers(matt_hand)
'''
nums = card_numbers(fox_hand)

for i in range(len(fox_hand)):
    try:
        while nums[i] > nums[i+1]:
            
            
    except: IndexError
'''

# card number of 1 string, not a list of strings:
def card_number2(string):
    if string[1].isnumeric() == True:
        # double digit number
        number = string[0:2]
    else:  #if lst[i][1] == ' ':
        # single digit number
        number = string[0]
    return int(number)



print(sorted(fox_hand, key = card_number2))














