'''
Author: Jack Ford
KUID: 3067365
Date: 10/6/21
Lab: Lab 05
Last modified: 10/19/21
Purpose: Executes a user entered command based on how they want to navigate their browser history
'''

pointer = 0
history = []
command = ""

while command != "EXIT":
	command = input("Enter a command: ")
	com = command.split()

	if com[0] == "NAVIGATE":
		if pointer < len(history) - 1:
			history = history[0: pointer + 1]

		url = com[1]
		history.append(url)
		pointer = len(history) - 1

	if command == "BACK":
		if pointer > 0:
			pointer = pointer - 1

	if command == "FORWARD":
		if pointer < len(history) - 1:
			pointer = pointer + 1

	if command == "HISTORY":
		print("")
		print("Oldest")
		print("===============")

		i = 0
		while i < len(history):
			if i == pointer:
				print(history[i] + "  <==")

			else:
				print(history[i])

			i = i + 1

		print("===============")
		print("Newest")
		print("")
