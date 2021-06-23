# whoops.. deleted the actual README file. Can obtain the file from github sample python project i think.

# Ideas for the program:

# Don't want to clutter the src doc so putting all my commented ideas here.


1. create a deck of cards using 'class'
2. Could test the dealt hands to make sure each combination of cards is dealt equally as deals -> infinity.
3. Could shuffle the 'cards_to_be_split' list more. - would it make a difference to 2.?
4. 



# Comments:
1. Dont need the first_run_done variable in the betting_round() function any more as the initial betting list is not [0,0,0]; it has  been updated with the SB & BB added to it.

2. # improvement: Dont make table_cards dictionary into a list,
    #               rather manipulate cards_to_be_split and dont remove the table cards from that variable,
    #               just say: table_cards['flop'] = cards_to_be_split[-3:]
    #                         table_cards['turn'] = cards_to_be_split[-4]
    #                         table_cards['river'] = cards_to_be_split[-5]
    #               Then there is no need to create this new variable: table_cards_list.
    
    
3. Treat this programme as a first draft - dont worry about condensing the code and making functions. can do this later. maybe make note of possible things that could be condensed.
4. ^on that note^ DONT WORRY ABOUT THE EFFICIENCY/LENGTH OF THE CODE!

5. Functions are not usable - HighCard() cannot be used outside its current scope.

6. Royal Flush == Straight Flush that includes an Ace.




# Areas to condense: 
1. Flush() function - use inside StraightFlush() function.   .