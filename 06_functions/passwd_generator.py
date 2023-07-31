import random

def create_passwd_generator(chars):
    """..."""
    
    def generate_passwd(passwd_length):
        passwd = ''
        for _ in range(passwd_length):
            passwd += random.choice(chars)
        return passwd
    
    return generate_passwd

passwd_symb_lett = create_passwd_generator('#!@?_/abcde')
print(passwd_symb_lett(7))
