import random

def create_passwd_generator(chars):
    """
    Take a string of allowed characters for a password. Return a function
    that randomly generates a password of a specified length from characters 
    in the string.
    """
    
    def generate_passwd(passwd_length):
        passwd = ''
        for _ in range(passwd_length):
            passwd += random.choice(chars)
        return passwd
    
    return generate_passwd

simple_passwd_chars = '#!@?abcdefghijklmnopqrstuvwxyz'
simple_passwd = create_passwd_generator(simple_passwd_chars)

advanced_passwd_chars = '#!@?1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
advanced_passwd = create_passwd_generator(advanced_passwd_chars)

print(create_passwd_generator(simple_passwd_chars)(12))
print(create_passwd_generator(advanced_passwd_chars)(12))

print(simple_passwd(15))
print(advanced_passwd(15))