'''
Author: Jack Ford
KUID: 3067365
Date: 12/1/21
Lab: Lab 11
Last modified: 12/8/21
Purpose: Get the file name from the user and act as the driver file
'''

from DMV import DMV

def main():
	file_name = input("Please enter a file name: ")
	myDMV = DMV(file_name)
	myDMV.run()

if __name__ == "__main__":
	main()
