total_price = 0

while (True):
    item_price = input('Please enter the item price: ')
    if item_price != 'q':
        total_price += int(item_price)
    else:
        print('sum of items is: ', total_price)
        break


