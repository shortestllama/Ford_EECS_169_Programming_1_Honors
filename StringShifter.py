'''
Author: Jack Ford
KUID: 3067365
Date: 9/29/21
Lab: lab04
Last modified: 10/4/21
Purpose: Obtain a string from the user and allow the user to perform modifications on the string from a menu
'''

user_command = 0
list_of_string = list(input("Please enter a string: "))


while user_command != 5:
	print(" ==================")
	print("|1. Shift left     |")
	print("|2. Shift right    |")
	print("|3. Reverse        |")
	print("|4. Mirror         |")
	print("|5. Exit           |")
	print(" ==================")

	user_command = int(input("Please select an option: "))

	if user_command == 1:
		temp = list_of_string[0]

		for i in range(0, len(list_of_string) - 1):
			list_of_string[i] = list_of_string[i + 1]

		list_of_string[len(list_of_string) - 1] = temp

	if user_command == 2:
		temp = list_of_string[len(list_of_string) - 1]

		for i in range(len(list_of_string) - 1, 0, -1):
			list_of_string[i] = list_of_string[i - 1]

		list_of_string[0] = temp

	if user_command == 3:
		temp_list = [""] * len(list_of_string)

		for i in range(0, len(list_of_string)):
			temp_list[i] = list_of_string[len(list_of_string) - i - 1]

		list_of_string = temp_list

	if user_command == 4:
		temp_list = list_of_string
		j = len(list_of_string)//2 - 1

		for i in range(len(list_of_string)//2, len(list_of_string)):
			temp_list[i] = list_of_string[j]
			j = j - 1

		list_of_string = temp_list

	print("".join(list_of_string))
