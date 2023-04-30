'''
Author: Jack Ford
KUID: 3067365
Date: 9/15/21
Lab: lab02
Last modified: 9/16/21
Purpose: Acts as a restaurant with menu items and returns the price of a user's order.
'''

pastaNum = 0
cheeseNum = 0
pieNum = 0

print("=========================")
print("WELCOME TO THE RESTAURANT")
print("=========================")
print(" ")

pasta = input("Do you want Cold Pasta? (y/n): ")
if pasta == "Y" or pasta == "y":
	pastaNum = int(input("How many? "))
	if pastaNum < 0:
		pastaNum = 0

cheese = input("Do you want Grilled Cheese? (y/n): ")
if cheese == "Y" or cheese == "y":
	cheeseNum = int(input("How many? "))
	if cheeseNum < 0:
		cheeseNum = 0

pie = input("Do you want Pie? (y/n): ")
if pie == "Y" or pie == "y":
	pieNum = int(input("How many? "))
	if pieNum < 0:
		pieNum = 0

age = int(input("How old are you? "))

pastaPrice = 2.50 * pastaNum
cheesePrice = 5.55 * cheeseNum

if age > 5:
	piePrice = 3.00 * pieNum
else:
	piePrice = 0.00

sub = pastaPrice + cheesePrice + piePrice
tax = .08 * sub
subtotal = sub + tax
discount = 0.00

if age >= 55:
	discount = .55 * subtotal

total = subtotal - discount

print(str(pastaNum) + f" Cold Pasta @ 2.50 ==> {pastaPrice:0.2f}")
print(str(cheeseNum) + f" Grilled Cheese @ 5.55 ==> {cheesePrice:0.2f}")
print(str(pieNum) + f" Pie @ 3.00 ==> {piePrice:0.2f}")
print(f"Subtotal: ${subtotal:0.2f}")
print(f"Tax: ${tax:0.2f}")
print(f"Discount: ${discount:0.2f}")
print("=========================")
print(f"Total: ${total:0.2f}")
print("Please come again!")
