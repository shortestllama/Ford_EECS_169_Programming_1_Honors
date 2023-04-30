'''
Author: Jack Ford
KUID: 3067365
Date: 9/29/21
Lab: lab04
Last modified: 10/4/21
Purpose: Allows the user to enter values for two lists and compares their sums, averages, and checks for overlapping numbers and whether or not they are palindromes
'''

list1 = []
list2 = []

exit = ""
while exit != "y" and exit != "Y":
	num = int(input("Enter a value for the first list: "))
	list1.append(num)
	exit = input("Are you done? (y/Y): ")

print("")
exit = ""
while exit != "y" and exit != "Y":
        num = int(input("Enter a value for the second list: "))
        list2.append(num)
        exit = input("Are you done? (y/Y): ")

sum1 = 0
for num in list1:
	sum1 = sum1 + num

ave1 = sum1/len(list1)

sum2 = 0
for num in list2:
	sum2 = sum2 + num

ave2 = sum2/len(list2)

count = 0
for num in list1:
	if num in list2:
		count = count + 1

palindrome = "are not"
if len(list1) == len(list2):
	i = 0
	reverse = 0

	while i < len(list1):
		if list1[i] == list2[len(list2) - i - 1]:
			reverse = reverse + 1

		i = i + 1

	if reverse == len(list1):
		palindrome = "are"

print("\nStatistics:")
if sum1 > sum2:
	print("The first list has the larger sum of " + str(sum1))
else:
	print("The second list has the larger sum of " + str(sum2))

if ave1 > ave2:
	print("The first list has the larger average of " + str(ave1))
else:
	print("The second list has the larger average of " + str(ave2))

print("Count of values that appear in both lists: " + str(count))
print("The lists " + palindrome + " palindromes")
