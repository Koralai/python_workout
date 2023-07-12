def get_login_shells(filename):
    """
    Read a password file and return a dictionary of login shells with
    their corresponding users
    """
    shells = {}
    
    with open(filename, encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                
                user_info = line.split(':')
                current_shell = user_info[9].rstrip()
                current_username = user_info[0]
                
                # values are lists, to allow for multiple users per shell
                if current_shell in shells:
                    shells[current_shell].append(current_username)
                else:
                    shells[current_shell] = [f'{current_username}']
    
    return shells
                    
print(get_login_shells('05_files/passwd.txt'))
