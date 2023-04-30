'''
Author: Jack Ford
KUID: 3067365
Date: 9/22/21
Lab: lab03
Last modified: 9/28/21
Purpose: Obtain a string from the user and return the amount of times a sequence given by the user occurs in that string.
'''

word = input("Enter a word: ")
search = input("Do you want to do a case-sensitive search? (y/Y) ")
seq = input("Enter a sequence to count: ")

if search == "y" or search == "Y":
	num = word.count(seq)
else:
	caps_word = word.upper()
	caps_seq = seq.upper()
	num = caps_word.count(caps_seq)
print("In the string " + word + " the sequence " + seq + " occurs " + str(num) + " time(s).")

