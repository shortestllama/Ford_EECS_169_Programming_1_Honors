'''
Author: Jack Ford
KUID: 3067365
Date: 9/16/21
Lab: lab02
Last modified: 9/16/21
Purpose: Asks the user how many sodas they have and returns the amount of fridge cubes, six-packs, and singles they have.
'''

numSodas = int(input("How many sodas do you have? "))
numCubes = numSodas // 24
numPacks = (numSodas % 24) // 6
numSingles = numSodas % 6

print("Fridge Cubes: " + str(numCubes))
print("Six-packs: " + str(numPacks))
print("Singles: " + str(numSingles))
