'''
Author: Jack Ford
KUID: 3067365
Date: 10/28/21
Lab: Lab07
Last modified: 11/03/21
Purpose: Get a file name from the user and run functions on a matrix and save the results to other files
'''

def get_file():
	file_name = input("Please enter a file name: ")
	return file_name

def set_file(file_name, output_text):
	matrix_file = open(file_name, "w")
	matrix_file.write(output_text)
	matrix_file.close()

def to_matrix(file_name):
	matrix = []
	matrix_file = open(file_name, "r")

	for line in matrix_file:
		line = line.replace("\n", "")
		mat_list = line.split(" ")
		matrix.append(mat_list)

	matrix_file.close()
	return matrix

def to_float(matrix):
	i = 0
	while i < len(matrix):
		j = 0
		while j < len(matrix[i]):
			matrix[i][j] = float(matrix[i][j])
			j = j + 1

		i = i + 1

	return matrix

def to_text(matrix):
	temp_matrix = [[0.0] * len(matrix[0])] * len(matrix)
	text = ""
	i = 0
	j = 0

	while i < len(matrix):
		while j < len(matrix[i]):
			temp_matrix[i][j] = str(matrix[i][j])
			j = j + 1

		text = text + " ".join(temp_matrix[i]) + "\n"
		i = i + 1
		j = 0

	return text

def averages(matrix):
	count = 0
	row_sum = 0
	row_average = 0
	sum = 0
	averages = []

	for line in matrix:
		for num in line:
			row_sum = row_sum + num
			row_average = row_sum / len(line)

		averages.append(row_average)
		row_average = 0
		sum = sum + row_sum
		row_sum = 0
		count = count + len(line)

	average = sum / count
	averages.insert(0, average)

	text = "Total average: " + str(averages[0]) + "\n"
	row_num = 1

	while row_num <= len(matrix):
		text = text + "Row " + str(row_num) + " average: " + str(averages[row_num]) + "\n"
		row_num = row_num + 1

	set_file("averages.txt", text)

def reverse(matrix):
	temp_matrix = [[0.0]] * len(matrix)

	for i, line in enumerate(matrix):
		temp_matrix[i] = line[::-1]

	set_file("reverse.txt", to_text(temp_matrix))

def flipped(matrix):
	temp_matrix = []

	for line in matrix:
		temp_matrix.insert(0, line)

	set_file("flipped.txt", to_text(temp_matrix))

def diagonal(matrix):
	temp_matrix = []

	j = 0
	while j < len(matrix):
		i = 0
		new_row = [0.0] * len(matrix)
		while i < len(matrix):
			new_row[i] = matrix[i][j]
			i = i + 1

		temp_matrix.append(new_row)
		j = j + 1

	set_file("diagonal.txt", to_text(temp_matrix))

def transpose(matrix):
	temp_matrix = []

	j = 0
	i = 0
	while j < len(matrix[i]):
		new_row = [0.0] * len(matrix)
		while i < len(matrix):
			new_row[i] = matrix[i][j]
			i = i + 1

		temp_matrix.append(new_row)
		j = j + 1
		i = 0

	set_file("transpose.txt", to_text(temp_matrix))

def main():
	matrix = to_float(to_matrix(get_file()))
	averages(matrix)
	reverse(matrix)
	flipped(matrix)
	count = 0

	for line in matrix:
		if len(line) == len(matrix):
			count = count + 1

	if count == len(matrix):
		diagonal(matrix)

	transpose(matrix)

main()
