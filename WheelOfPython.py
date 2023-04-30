'''
Author: Jack Ford
KUID: 3067365
Date: 10/6/21
Lab: Lab 05
Last modified: 10/6/21
Purpose: Allow the user to guess 5 letters in a secret phrase,
	 then reveal those letters in the phrase,
	 then allow them to guess the phrase
'''

secret_phrase = list("WHEEL OF PYTHON")
hidden_phrase = list("????? ?? ??????")

letters = list(input("Choose 5 letters to help you guess: ").upper())

while len(letters) != 5:
	if len(letters) > 5:
		letters = list(input("Too many letters, try again: ").upper())

	if len(letters) < 5:
		letters = list(input("Too few letters, try again: ").upper())

print("Here is your phrase:")

i = 0
while i < len(secret_phrase):
	for letter in letters:
		if secret_phrase[i] == letter:
			hidden_phrase[i] = secret_phrase[i]

	i = i + 1

print("".join(hidden_phrase))

guess = list(input("Enter your guess: ").upper())
while len(guess) != len(secret_phrase):
	guess = list(input("Please enter a guess of equal length to the phrase: ").upper())

count = 0
j = 0
while j < len(secret_phrase):
	if guess[j] == secret_phrase[j]:
		count = count + 1

	j = j + 1

if count == len(secret_phrase):
	print("You win!")

else:
	print("You lose!")
