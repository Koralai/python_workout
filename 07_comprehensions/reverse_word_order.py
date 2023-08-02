def reverse_word_order(line):
    """Reverse the order of words in a line of text."""
    
    words = line.split()
    output = []
    
    for word in words:
        output.insert(0, word)
        
    return ' '.join(output)

line_1 = "shall I compare thee to a summer's day"

print(reverse_word_order(line_1))
