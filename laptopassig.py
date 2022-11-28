'''print('==================Computer Bazar=================')
print('1.Dell Rs20000 2.Toshiba Rs40000 3.Mac Rs50000')
option = int(input('Enter any option:'))
dell_price=0
Toshiba_price=0
Mac_price=0
dell_price=0
packing_Plactic=0
packing_bag=0
packing_Gift=0
Tax_amount=0
if option == 1:
    quantity = int(input('Enter the quantity:'))
    dell_price = quantity * 20000
elif option == 2:
    quantity = int(input('Enter the quantity:'))
    Toshiba_price = quantity * 40000
elif option == 3:
    quantity = int(input('Enter the quantity'))
    Mac_price = quantity * 50000
else:
    print('Invalid option')
    exit()

print("where u want the delivry")
print("1.Home Rs1000 2.Pickup free")
option = int(input('Enter the delivery option'))
if option == 1:
    delivery_price = 1000
print("What about the packing")
print("1.Plastic Rs500 2.Bag Rs1000 3.Gift Rs 5000")
paking_option = int(input('Enter the choice'))
if option == 1:
    packing_Plactic = 500
elif option == 2:
    packing_Bag = 1000
elif option == 3:
    packing_Gift = 5000
total = dell_price+Toshiba_price+Mac_price
print('What about the Location')
print('1. KTM 13%Tax 2.LPT Free 3.BKT Free')
location_option = int(input('Enter the choice:'))
if option == 1:
    tax_amount = total * 0.13
grandtotal = tax_amount+packing_Gift+packing_Bag+packing_Plactic+delivery_price+delivery_price+Toshiba_price+Mac_price
print('===================BILL===================')
print(total)
print(tax_amount)
print(grandtotal)
'''