import csv

def get_csv_rows_no_blanks(filename_r, filename_w):
    """
    Read lines of a CSV file. Write all rows that do not contain blanks
    to another CSV file.
    """
    
    with open(filename_r) as read_csv, open(filename_w, 'w') as write_csv:
        file_reader = csv.reader(read_csv, delimiter=',')
        filtered_rows = []
        
        for row in file_reader:
            has_blank_data = False
            
            for cell in row:
                if len(cell) == 0:
                    has_blank_data = True
                    break
            if has_blank_data is False:
                filtered_rows.append(row)
                
        print(filtered_rows)
            
get_csv_rows_no_blanks(
    '05_files/csv_mini_project/lotr_characters.csv',
    '07_comprehensions/lotr_characters_no_blanks.csv')
            