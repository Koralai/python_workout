def reverse_lines(input_file):
    """
    Read the contents of the input file. For each line of the file, reverse
    the order of the characters and write the reversed line to the output file.
    """
    
    with open(input_file, encoding='utf-8') as input_f:
        for line in input_f:
            print(''.join(reversed(line.rstrip())))
            
reverse_lines('05_files/wcfile.txt')
