def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

straight_cards = ['3 H', '4 H', '4 D', '5 H', '6 H', '7 H']
print(indices(straight_cards, '4 H'))
