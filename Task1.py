pricelist = [150, 50, 60, 100, 90, 40]
itemlist = ['burger', 'cola', 'juice', 'salad', 'fries', 'fruit']
print('Hello, welcome to the snack shop')
print('Here is is our menu: ')
print('Option number, Item, Price \n 1, Burger, 150 \n 2, Cola, 50 \n 3, Juice, 60 \n 4, Salad, 100 \n 5, Fries, 90 \n 6, Fruit, 40')
choice = -1 + int(input('Please enter the option number of your chosen snack: '))
foodchoice = itemlist[choice]
foodprice = pricelist[choice]
print('Your order of ', foodchoice, 'will be', foodprice, 'pesos')

