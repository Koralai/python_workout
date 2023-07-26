def write_every_nth_line(filename_r, filename_w, n):
    """
    Read a file and write a new file containing every nth line of the 
    original file.
    """
    
    with open(filename_r) as input_file, open(filename_w, 'w') as output_file:
        
        line_number = 1
        
        for line in input_file:
            if line_number % n == 0:
                output_file.write(line)
            line_number += 1
