def passwd_to_dict(filename):
    """
    Read a password file and return a dictionary of usernames and id numbers
    """
    users = {}
    
    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                line_elements = line.split(':')
                username = line_elements[0]
                userid = int(line_elements[2])
                users[username] = userid
        
    return users

print(passwd_to_dict('05_files/passwd.txt'))
