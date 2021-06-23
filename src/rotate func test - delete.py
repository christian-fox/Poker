# rotate func test
def rotate(lst, n):  # function rotates the list (backwards) n times
    return print(lst[n:] + lst[:n])

lst = [2,7,8,9,10,11,13]


for i in range(len(lst)):
    rotate(lst,i)

