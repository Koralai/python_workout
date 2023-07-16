from get_word_count import get_word_count
from sort_by_highest_vals import sort_by_highest_vals
from format_word_count_data import format_word_count_data

print("Give me a file name, and I'll tell you the most commonly used words in that file.")

user_file = input("File name: ")
num_words = int(input("Number of words (e.g., write '10' to see the top 10 words): "))

word_count_data = get_word_count(user_file)
sorted_data = sort_by_highest_vals(word_count_data)

print(format_word_count_data(sorted_data, num_words))
