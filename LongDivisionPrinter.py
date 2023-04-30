'''
Author: Jack Ford
KUID: 3067365
Date: 9/15/21
Lab: lab02
Last modified: 9/15/21
Purpose: Asks the user for two digits and returns the result of dividing the first digit by the second digit and returns the remainder.
'''

flag = True

while flag:
	x = int(input("Enter a numerator: "))
	y = int(input("Enter a denominator: "))
	if y == 0:
		print("Sorry, you may not divide by zero.")
	else:
		result = x//y
		r = x%y
		print(str(x) + "/" + str(y) + " = " + str(result) + " Remainder: " + str(r))
	ans = input("Do you want to exit? (Y/y): ")
	if ans == "Y" or ans == "y":
		flag = False
