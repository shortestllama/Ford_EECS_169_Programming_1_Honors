'''
Author: Jack Ford
KUID: 3067365
Date: 9/15/21
Lab: lab02
Last modified: 9/15/21
Purpose: Asks the user for a wind speed input and returns the weather category that wind speed falls under.
'''

speed = int(input("Input a wind speed (m/s): "))
intro = "A wind speed of "

if speed >= 70:
	print(intro + str(speed) + " m/s is a Category 5 hurricane.")
elif speed >= 58:
	print(intro + str(speed) + " m/s is a Category 4 hurricane.")
elif speed >= 50:
	print(intro + str(speed) + " m/s is a Category 3 hurricane.")
elif speed >= 43:
	print(intro + str(speed) + " m/s is a Category 2 hurricane.")
elif speed >= 33:
	print(intro + str(speed) + " m/s is a Category 1 hurricane.")
elif speed >= 18:
	print(intro + str(speed) + " m/s is a Tropical Storm.")
elif speed >= 0:
	print(intro + str(speed) + " m/s is a Tropical Depression.")
else:
	print("Invalid wind speed.")
