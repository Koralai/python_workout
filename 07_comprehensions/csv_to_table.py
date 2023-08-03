import csv

def csv_to_table(filename_r, filename_w):
    """
    Read lines of a CSV file and print them to a new file, formatted
    as a readable table. Only do this for CSV rows that have the required
    number of columns.
    """
    
    with open(filename_r) as read_csv, open(filename_w, 'w') as write_txt:
        file_reader = csv.reader(read_csv, delimiter=',')
        for row in file_reader:
            row = str(row)
            write_txt.write(row)
            
csv_to_table(
    '05_files/csv_mini_project/lotr_characters.csv',
    '07_comprehensions/csv_to_table.txt')
            