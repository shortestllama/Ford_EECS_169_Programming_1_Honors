'''
Author: Jack Ford
KUID: 3067365
Date: 12/1/21
Lab: Lab 11
Last modified: 12/8/21
Purpose: Print the menu to the user and perform actions based on the options they choose
'''

from DriversLicense import DriversLicense

class DMV:
	def __init__(self, file_name):
		self.file_name = file_name
		self.data_base = []
		driver_info = open(file_name, "r")
		driver_info.readline()

		for line in driver_info:
			text = line.replace('\n', '')
			temp = text.split('\t')
			temp_driver = DriversLicense(temp[1], temp[2], int(temp[3]), temp[4], int(temp[0]))
			self.data_base.append(temp_driver)

	def print_menu(self):
		print("Select an option:")
		print("1) Print all Drivers Info")
		print("2) Print all young, unregistered voters")
		print("3) Print drivers by first initial")
		print("4) Print driver with id")
		print("5) Register to vote")
		print("6) Quit")

	def license_info(self):
		for driver in self.data_base:
			print(driver)

	def run(self):
		choice = 0
		while choice != 6:
			self.print_menu()
			choice = int(input("Enter your choice: "))

			if choice == 1:
				self.license_info()

			elif choice == 2:
				for driver in self.data_base:
					if driver.get_age() >= 18 and driver.get_age() <= 24 and driver.get_is_voter() == 'N':
						print(driver)

			elif choice == 3:
				initial = input("Please enter a single character: ").lower()
				count = 0

				for driver in self.data_base:
					if driver.get_first_name()[0].lower() == initial:
						print(driver)
						count += 1

				if count == 0:
					print("No record found.")

			elif choice == 4:
				id = int(input("Please enter an ID: "))
				count = 0

				for driver in self.data_base:
					if driver.get_license_num() == id:
						print(driver)
						count += 1

				if count == 0:
					print("No record found.")

			elif choice == 5:
				lic_num = int(input("Please enter a drivers license number: "))
				count = 0

				for driver in self.data_base:
					if driver.get_license_num() == lic_num:
						count += 1

						if driver.get_is_voter() == "N":
							driver.set_is_voter("Y")

						else:
							print("Driver currently registered")

				if count == 0:
					print("No record found")

				output_file = open(self.file_name, "w")
				output_text = str(len(self.data_base)) + "\n"

				for driver in self.data_base:
					output_text += f"{driver.get_license_num()}\t{driver.get_first_name()}\t{driver.get_last_name()}\t{driver.get_age()}\t{driver.get_is_voter()}\n"

				output_file.write(output_text)
				output_file.close()

			elif choice == 6:
				pass

			else:
				print("Please enter a valid option.")
