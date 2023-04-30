'''
Author: Jack Ford
KUID: 3067365
Date: 9/22/21
Lab: lab03
Last modified: 9/28/21
Purpose: Ask the user for a day and return the amount of people infected with the flu on that day.
'''

print("OUTBREAK!")

fluCount = [1, 8, 22]
day = int(input("What day do you want a sick count for? "))
i = 3
intro = "Total people with flu: "

if day < 4 and day > 0:
	print(intro + str(fluCount[day-1]))

if day <= 0:
	print("Invalid day")

while len(fluCount) < day:
	num = fluCount[i-1] + fluCount[i-2] + fluCount[i-3]
	fluCount.append(num)
	if len(fluCount) == day:
		print(intro + str(fluCount[day-1]))
	i = i + 1
