import csv

def get_characters_by_sex(filename_r, filename_w, sex='f'):
    """
    Read a CSV file of character data. Write a CSV file containing only 
    the characters of the sex specified in the function call ('m' or 'f')
    """
    
    output_characters = []
    
    with open(filename_r, encoding='utf-8') as character_file:
        csv_reader = csv.reader(character_file, delimiter=',')
        
        for row in csv_reader:
            character_sex = row[3]
            if character_sex == sex:
                first_name = row[0]
                last_name = row[1]
                fantasy_race = row[2]
                output_characters.append((first_name, last_name, fantasy_race))
                
    with open(filename_w, 'w', newline='', encoding='utf-8') as new_character_file:
        csv_writer = csv.writer(new_character_file, delimiter='\t')
        
        for character in output_characters:
            if character[1] == '': # no last name
                csv_writer.writerow([character[0], character[2]])
            else:
                csv_writer.writerow(character)
                
                
                
get_characters_by_sex(
    '05_files/csv_mini_project/lotr_characters.csv',
    '05_files/csv_mini_project/lotr_f_characters.csv', 'f'
    )
