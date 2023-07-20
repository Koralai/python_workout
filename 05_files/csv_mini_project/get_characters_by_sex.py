import csv

def get_characters_by_sex(filename_r, sex='f'):
    """
    Read a CSV file of character data. Write a CSV file containing only 
    the characters of the sex specified in the function call ('m' or 'f')
    """
    
    with open(filename_r, encoding='utf-8') as character_file:
        csv_reader = csv.reader(character_file, delimiter=',')
        for row in csv_reader:
            character_sex = row[3]
            if character_sex == sex:
                print(row)
                
get_characters_by_sex('05_files/csv_mini_project/lotr_characters.csv')
