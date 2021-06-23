betting = ['f','0','10']

def maximum(lst):
    lst2 = []
    for i in lst:
        if i.isnumeric():
            lst2.append(i)
    x = max(lst2)
    return(x)

print(maximum(betting))
    
