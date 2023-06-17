import random

lotr_characters = [
    { 'first_name': 'arwen', 'last_name': '', 'race': 'elf'},
    { 'first_name': 'eowyn', 'last_name': '', 'race': 'human'},
    { 'first_name': 'aragorn', 'last_name': '', 'race': 'human'},
    { 'first_name': 'elrond', 'last_name': '', 'race': 'elf'},
    { 'first_name': 'galadriel', 'last_name': '', 'race': 'elf'},
    { 'first_name': 'gandalf', 'last_name': 'the gray', 'race': 'wizard'},
    { 'first_name': 'gollum', 'last_name': '', 'race': 'hobbit'},
    { 'first_name': 'frodo', 'last_name': 'baggins', 'race': 'hobbit'},
    { 'first_name': 'sam', 'last_name': 'gamgee', 'race': 'hobbit'},
    { 'first_name': 'pippin', 'last_name': 'took', 'race': 'hobbit'},
    { 'first_name': 'merry', 'last_name': 'brandybuck', 'race': 'hobbit'},
    { 'first_name': 'theoden', 'last_name': '', 'race': 'human'},
    { 'first_name': 'gimli', 'last_name': '', 'race': 'dwarf'},
    { 'first_name': 'legolas', 'last_name': '', 'race': 'elf'},
    { 'first_name': 'boromir', 'last_name': '', 'race': 'human'},
    { 'first_name': 'faramir', 'last_name': '', 'race': 'human'},
    { 'first_name': 'saruman', 'last_name': 'the white', 'race': 'wizard'},
    { 'first_name': 'denethor', 'last_name': '', 'race': 'human'},
    { 'first_name': 'bilbo', 'last_name': 'baggins', 'race': 'hobbit'},
    { 'first_name': 'thorin', 'last_name': 'oakenshield', 'race': 'dwarf'},
    ]

def guessing_game():
    """
    A game that asks the user to guess the name of a 
    character from The Hobbit or The Lord of the Rings
    """
    
    print("I'm thinking of a character from The Lord of the Rings or "
          "The Hobbit. Can you guess who?")
    
    # randomly choose one of the characters
    i = random.randint(0, len(lotr_characters) - 1)
    character = lotr_characters[i]
    
    # get the first letter of the character's name
    character_first_letter = character['first_name'][0]
    
    # get the character's full name
    if character['last_name']: # not all characters have last names
        character_full_name = f"{character['first_name']} {character['last_name']}"
    else:
        character_full_name = f"{character['first_name']}"
    
    
    guessing = True    
    while guessing is True:            
        # ask the user for their guess
        guess = input("\nCharacter name: ").lower()
        guessed_first_letter = guess[0]
        
        # if they're right, congratulate them and end the game    
        if guess == character['first_name']:
            print(f"You're right! I'm thinking of {character_full_name.title()}.")
            guessing = False

        # if not, tell them whether the first letter in the name is before or after what they guessed
        else:
            if ord(guessed_first_letter) == ord(character_first_letter):
                print(f"Try again! This character's name "
                      f"also starts with the letter {guessed_first_letter}.")
            elif ord(guessed_first_letter) < ord(character_first_letter):
                print("Try again! This character's name starts with "
                      "a letter that's later in the alphabet.")
            else:
                print("Try again! This character's name starts with "
                      "a letter that's earlier in the alphabet.")    



def main():
    guessing_game()

if __name__ == '__main__':
    main()

# improvements:
    # increase a counter for each guesses
    # on the fourth guess, ask if the user wants a hint 
    # quit the game if the user's guess is not correct after the hint?