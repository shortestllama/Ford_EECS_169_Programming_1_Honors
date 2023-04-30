'''
Author: Jack Ford
KUID: 3067365
Date: 10/20/21
Lab: lab 06
Last modified: 10/20/21
Purpose: Prints a menu and asks the user for a positive integer to perform their choice from the menu on.
'''

def last_digit(num):
	return num % 10

def remove_last_digit(num):
	return num // 10

def add_digit(current_num, new_digit):
	return current_num * 10 + new_digit

def reverse(num):
	n = 0

	for i in range(0, len(str(num))):
		n = add_digit(n, last_digit(num))
		num = remove_last_digit(num)

	return n

def is_palindrome(num):
	if num == reverse(num):
		return True
	return False

def count_digits(num):
	count = 1
	while remove_last_digit(num) > 0:
		count = count + 1
		num = remove_last_digit(num)

	return count

def sum_digits(num):
	n = last_digit(num)

	while remove_last_digit(num) > 0:
		num = remove_last_digit(num)
		n = n + last_digit(num)

	return n

def print_menu():
	print("1) Count digits")
	print("2) Sum digits")
	print("3) Is palindrome")
	print("4) Reverse")
	print("5) Exit")

def get_int():
	x = int(input("Please enter a positive integer: "))
	return x

def main():
	choice = 0
	while choice != 5:
		print_menu()
		choice = int(input("Choice: "))

		if choice == 1:
			x = get_int()
			print(count_digits(x))

		if choice == 2:
			x = get_int()
			print(sum_digits(x))

		if choice == 3:
			x = get_int()

			if is_palindrome(x):
				print(str(x) + " is a palindrome.")

			else:
				print(str(x) + " is not a palindrome.")

		if choice == 4:
			x = get_int()
			print(reverse(x))

main()
