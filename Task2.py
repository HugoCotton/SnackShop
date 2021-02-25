pricelist = [150, 50, 60, 100, 90, 40]
itemlist = ['burger(s)', 'cola(s)', 'juice(s)', 'salad(s)', 'fries', 'fruit(s)']
orderlist = []
numlist = []
totalcost = 0
repeat = 'y'
totalprice = 0
print('Hello, welcome to the snack shop')
print('Here is is our menu: ')
print('Option number, Item, Price \n 1, Burger, 150 \n 2, Cola, 50 \n 3, Juice, 60 \n 4, Salad, 100 \n 5, Fries, 90 \n 6, Fruit, 40')
while repeat == 'y' or repeat == 'Y':
    choice = -1 + int(input('Please enter the snack you would like to buy: '))
    orderlist.append(itemlist[choice])
    number = int(input('How many would you like to buy?: '))
    numlist.insert(choice,number)
    totalcost += pricelist[choice] * number
    repeat = input('would you like to order more? Y or N: ')
for i in range(len(orderlist)):
    print(f'You ordered {numlist[i]} {orderlist[i]} ')
print(f'This comes to a total of {totalcost} pounds')
