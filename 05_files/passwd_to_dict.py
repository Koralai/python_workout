def passwd_to_dict(filename):
    """
    Read a password file and return a dictionary of usernames and id numbers
    """
    output = {}
    
    with open(filename, encoding='utf-8') as f:
        lines = f.read().splitlines()
    
    for line in lines:
        if line.startswith('#'):
            continue
        
        line_elements = line.split(':')
        username = line_elements[0]
        userid = line_elements[2]
        output[username] = userid
        
    return output

print(passwd_to_dict('05_files/passwd.txt'))
