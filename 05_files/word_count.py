def get_word_count(filename):
    """
    Read a file and return a few simple data points about the words in the file
    """
    num_chars = 0
    num_words = 0
    num_lines = 0
    unique_words = set()
    
    with open(filename, encoding='utf-8') as f:
        for line in f:
            words = line.split()
            num_chars += len(line)
            num_lines += 1
            num_words += len(words)
            unique_words.update(words)
    
    message = (f"This file contains {num_words:,} words and {len(unique_words):,} "
               f"unique words.\nIt also contains {num_chars:,} characters.\n"
               f"It has {num_lines:,} lines.")
    return message

print(get_word_count('02_strings/lamplighter.txt'))
