def reverse_lines(input_file, output_file):
    """
    Read the contents of the input file. For each line of the file, reverse
    the order of characters and write the reversed line to the output file.
    """
    
    with open(input_file) as input_f, open(output_file, 'w') as output_f:
        for line in input_f:
            reversed_line = ''.join(reversed(line.rstrip()))
            output_f.write(f"{reversed_line}\n")
            
reverse_lines('05_files/wcfile.txt', '05_files/wcfile_reversed.txt')
