def get_user_info(filename):
    """
    Read a password file and return a dict in which the keys are usernames
    and the values are themselves dicts containing userid, home directory, and shell
    """
    users = {}
    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                
                user_info = line.rstrip().split(':')
                
                username = user_info[0]                
                user_dict = {
                    'userid': user_info[2],
                    'home directory': user_info[8],
                    'login_shell': user_info[9]
                }
                
                users[username] = user_dict
    
    return users

print(get_user_info('05_files/passwd.txt'))
