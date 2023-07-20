import csv

def passwd_to_csv(filename_r, filename_w):
    """
    Extract user data from a csv file and write it to another csv file
    """
    
    users = {}
    
    with open(filename_r, encoding='utf-8') as csv_file_r:
        csv_reader = csv.reader(csv_file_r, delimiter=':')
        for row in csv_reader:
            if len(row) > 1: # exclude comments
                username = row[0]
                userid = row[2]
                users[username] = userid
    
    with open(filename_w, 'w', newline='', encoding='utf-8') as csv_file_w:
        csv_writer = csv.writer(csv_file_w, delimiter='\t')
        for key, value in users.items():
            csv_writer.writerow([key, value])
    
            
passwd_to_csv('05_files/passwd.csv', '05_files/users.csv')
