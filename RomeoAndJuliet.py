'''
Author: Jack Ford
KUID: 3067365
Date: 11/03/21
Lab: Lab 08
Last modified: 11/10/21
Purpose: Save the amount of each word from a
	 .txt file into a file named
	 word_data.txt and the words that only
	 occur one time to a file named
	 unique_words.txt
'''

def build_count(text):
	word_counts = {}

	for word in text:
		word_counts[word] = text.count(word)

	return word_counts

def clean_word(word):
	word = word.lower()
	word = word.replace('!', ' ')
	word = word.replace('?', ' ')
	word = word.replace(':', ' ')
	word = word.replace(';', ' ')
	word = word.replace(',', ' ')
	word = word.replace('|', ' ')
	word = word.replace('.', ' ')
	word = word.replace('--', ' ')
	word = word.strip()

	if word[0] == "'":
		if word[len(word) - 1] == "'":
			word_list = list(word)
			word_list.pop(0)
			word_list.pop(len(word_list) - 1)
			word = ''.join(word_list)

	word = word.strip()
	return word

def unique_words(word_counts):
	unique_words = []

	for word, count in word_counts.items():
		if count == 1:
			unique_words.append(word)

	return unique_words

def main():
	welcome_message = "Welcome to the word counter!"
	print(welcome_message.center(40, "="))
	file_name = input("Please enter a file name: ")
	text = open(file_name, "r")
	text_list = text.read().split()
	text.close()

	for ind, word in enumerate(text_list):
		text_list[ind] = clean_word(word)

	word_data = open("word_data.txt", "w")
	word_counts = build_count(text_list)

	for word, count in word_counts.items():
		word_data.write(word + " : " + str(count) + "\n")

	word_data.close()
	uniques = open("unique_words.txt", "w")
	output = "Here is a list of words that appear exactly one time in romeoandjuliet.txt\n" + "\n".join(unique_words(word_counts))
	uniques.write(output + "\n")
	uniques.close()

main()
