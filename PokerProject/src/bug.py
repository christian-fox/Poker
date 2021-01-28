def maximum(lst):
    lst2 = []
    for i in lst:
        if i.isnumeric():
            lst2.append(int(i))
    x = str(max(lst2))
    return(x)



def bets_settled(lst):
    settled = [False for _ in range(len(lst))]
    final = True
    for k in range(len(lst)):
        if lst[k] == maximum(lst):  # if k != max
            #print(k,"is max value in list")
            settled[k] = True
        elif lst[k].find('f') > -1:  # if 'f' does appear in k, ie. player has folded
            #print("f appears in item", k)
            settled[k] = True
        #else:
            #print(k, "needs to be dealt with")
    if any(x == False for x in settled):
        final = False
    return final
    
#  This function returns TRUE if 'lst' is settled - ie. if betting round is over.    
    


bettings = ['200','200','100','200','f','199f','200']

print(bets_settled(bettings))

print(bettings)


#if any(k != maximum(bettings) or k.find('f') == -1 for k in bettings):
if bets_settled(bettings) == False:
    print("1 player either has not folded or is yet to call")
    # something is going wrong with this if statement..
# what do i want this line to do?
# go through the list and decifer whether each item either has an f or is max(betting)

'''   
print(maximum(bettings), type(maximum(bettings)))
print(bettings[0].find('f'),"the 2nd item does not contain the string 'f'")
print("the last item does contain 'f' and 'f' appears in the ",
       bettings[2].find('f')," index/position")
'''









