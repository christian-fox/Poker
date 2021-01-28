player_dic69 = {'name': ['fox','matt','rog'], 'chips':[1000,1000,1000]}
print(player_dic69)

# Creating a manual input (through the command window) for this dictionary above.
####################################################################################

player_info = {}  # dictionary

players = int(input("How many players? "))  # number of players

player_info['name'] = []

# this loop obtains the players names and prints them.
for i in range(1, players+1):
    name = input('Enter ' + var_name + ' Name: ')
    player_info['name'].append(name)
    #var_name = "Player%d" % i     # var_name = Player1
    #print(var_name, 'is called', name) 


player_info['chips'] = [1000 for _ in range(players)]  # creates a list of size: player_number, with all elements = 1000
print(player_info)



# The 2 dictionaries, plater_dic69 and player_info are the same (when you choose the options: 3, fox, matt, rog)

























####################################################################################

'''
for i in range(3):  # i = 0,1,2
    print(player_dic69['name'][i], 'chips',player_dic69['chips'][i])
'''











