'''
Author: Jack Ford
KUID: 3067365
Date: 11/12/2021
Lab: Lab 09
Last modified: 11/16/2021
Purpose: Access a pokedex and allow the user
         to perform menu actions with the pokedex.
'''

import random

def build_pokedex(filename):
        pokedex = {}
        poke_names = open(filename, "r")

        for line in poke_names:
                line = line.replace("\n", '')
                temp = line.split("\t")
                pokedex[temp[0]] = temp[1]

        return pokedex

def build_team(pokedex, size=6, is_unique=False):
        poke_list = []

        for key in pokedex.keys():
                poke_list.append(key)

        if is_unique:
                return random.sample(poke_list, k=size)

        return random.choices(poke_list, k=size)

def battle(team1, team2):
        battle = []
        battle.append("+++Team 1+++")

        for pokemon in team1:
                battle.append(pokemon)

        battle.append("")
        battle.append("+++Team 2+++")

        for pokemon in team2:
                battle.append(pokemon)

        battle.append("")
        count = 1

        while len(team1) > 0 and len(team2) > 0:
                battle.append("+++Round " + str(count) + "+++")
                battle.append(team1[0] + " VS " + team2[0])
                winner = random.randint(1, 2)

                if winner == 1:
                        battle.append(team1[0] + " wins!")
                        team2.pop(0)

                if winner == 2:
                        battle.append(team2[0] + " wins!")
                        team1.pop(0)

                battle.append("")
                count = count + 1

        if len(team1) > 0:
                battle.append("+++Team 1 Wins!+++")

                for pokemon in team1:
                        battle.append(pokemon)

        else:
                battle.append("+++Team 2 Wins!+++")

                for pokemon in team2:
                        battle.append(pokemon)

        return battle

def print_menu():
        print("1) Print Pokedex")
        print("2) Translate")
        print("3) Build a team")
        print("4) Pokemon battle")
        print("5) Exit")
        print("6) Fight log")

def main():
        poke_file = input("Please enter a file name: ")
        pokedex = build_pokedex(poke_file)
        print()
        choice = 0

        while choice != 5:
                print_menu()
                choice = int(input("Please select an option: "))

                if choice == 1:
                        for key in pokedex.keys():
                                print("US name: ", key, "\tJPN name: ", pokedex[key])

                if choice == 2:
                        name = input("Which US name would you like to translate? ")

                        if name in pokedex.keys():
                                print(name, "in JPN is: ", pokedex[name])

                        else:
                                print("Sorry, but that name isn't in the Pokedex.")

                if choice == 3:
                        team = build_team(pokedex)

                        for pokemon in team:
                                print(pokemon)

                if choice == 4:
                        for line in battle(build_team(pokedex, 6, True), build_team(pokedex, 6, True)):
                                print(line)

                if choice == 6:
                        output_file = input("Please enter a file name: ")
                        poke_file = open(output_file, "w")
                        battle_list = battle(build_team(pokedex, 6, True), build_team(pokedex, 6, True))

                        for line in battle_list:
                                print(line)
                                poke_file.write(line + "\n")

                        poke_file.close()

main()
