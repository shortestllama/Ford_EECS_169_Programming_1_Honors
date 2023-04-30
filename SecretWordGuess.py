'''
Author: Jack Ford
KUID: 3067365
Date: 9/22/21
Lab: lab03
Last modified: 9/28/21
Purpose: Asks the user to enter a string until they guess the correct phrase while giving them hints along the way.
'''

print("Guess the secret phrase!")
password = "BRINGCOFFEE"
guess = ""
numGuesses = 0
flag = True

while flag:
	guess = input("Guess: ")
	count = 0
	numGuesses = numGuesses + 1

	if guess.upper() == password:
		flag = False

	elif len(guess) < len(password):
		print("Too few characters")

	elif len(guess) > len(password):
		print("Too many characters")

	else:
		for num in range(0,len(password)):
			if guess.upper()[num] == password[num]:
				count = count + 1
		print("Correct letters: " + str(count))

print("Correct!")
print("Number of guesses: " + str(numGuesses))
