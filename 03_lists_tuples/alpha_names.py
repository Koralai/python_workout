def alphabetize_names(list_of_people):
    """
    Take a list of dictionaries containing first and last names.
    Return the same list of dictionaries sorted alphabetically 
    (by last name, then by first name).
    """
    
    return sorted(list_of_people, key=lambda person: person['last'])
    
PEOPLE = [
    {'first': 'frodo', 'last': 'baggins', 'age': 50,},
    {'first': 'bilbo', 'last': 'baggins', 'age': 111,},
    {'first': 'samwise', 'last': 'gamgee', 'age': 38, },
    {'first': 'meriadoc', 'last': 'brandybuck', 'age': 36, },
    {'first': 'peregrin', 'last': 'took', 'age': 29,},
]    

def main():
    print(alphabetize_names(PEOPLE))

if __name__ == '__main__':
    main()
