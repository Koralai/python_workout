def reverse_word_order(line):
    """Reverse the order of words in a line of text."""
    words = line.split()
    reverse_ord_words = words[::-1]
        
    return ' '.join(reverse_ord_words)

line_1 = "shall I compare thee"

print(reverse_word_order(line_1))
