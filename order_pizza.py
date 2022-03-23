#This is the pizza information
'''
Small_Pizza = 15
Medium_Pizza = 20
Large_Pizza = 25
Add_Pepperoni = ('Y')
Add_Cheese = ('N')
Small Pizza Topping = 2
Medium and Large Pizza Topping = 3
Cheese = 1
'''

print('Welcome To Python Pizza. Please Place Your Order')
Size = input('What pizza size do you want to order? S, M or L:')
Topping = input('Do you want pepperoni? Y or N:')
Extra_Cheese = input('Do you want extra cheese? Y or N:')


bill = 0

if Size == 'S' or Size == 's':
  bill += 15
elif Size == 'M' or Size == 'm':
  bill += 20
elif Size == 'L' or Size == 'l':
  bill += 25
else: print("choose a size!")

if Topping == 'Y' or Topping == 'y':
  if Size == 'S' or Size == 's':
    bill += 2
  else:
    bill += 3

if Extra_Cheese == 'Y' or Extra_Cheese == 'y':
  bill += 1
else:
  bill += 0
final_bill = bill
print(f'Your total bill is: £{final_bill}.')


  