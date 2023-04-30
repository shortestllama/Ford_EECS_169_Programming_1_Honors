'''
Author: Jack Ford
KUID: 3067365
Date: 9/29/21
Lab: lab04
Last Modified: 9/29/21
Purpose: Allow the user to modify a shopping list how they like with certain menu items.
'''

list = []
choice = 0
while choice != 4:
	print("\n ==================")
	print("|Menu:             |")
	print("|1. Add item       |")
	print("|2. Check off item |")
	print("|3. Print list     |")
	print("|4. Exit           |")
	print(" ==================")

	choice = int(input("What would you like to do? "))

	if choice == 1:
		new_item = input("What would you like to add to the list? ")
		list.append(new_item)

	if choice == 2:
		item = int(input("Which item would you like to check off? "))
		s = list[item - 1]

		i = 1
		line = "-"
		while i < len(s) - 2:
			line = line + "-"
			i = i + 1

		new_str = s[0] + line + s[len(s) - 1]
		list[item - 1] = new_str

	if choice == 3:
		print("Shopping list:\n")

		i = 1
		for item in list:
			print(str(i) + ". " + item)
			i = i + 1

print("Goodbye!")
