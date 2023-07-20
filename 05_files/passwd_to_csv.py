import csv

def passwd_to_csv(filename_r):
    """
    Read csv data from the first file and write it to the second
    file in formatted columns
    """
    
    users = {}
    
    with open(filename_r, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        for row in csv_reader:
            if len(row) > 1: # exclude comments
                username = row[0]
                userid = row[2]
                users[username] = userid
    
    return users
            
print(passwd_to_csv('05_files/passwd.csv'))
