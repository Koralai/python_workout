import random
import list_characters_lotr as ls

def compare_first_letters(str_1, str_2):
    str_1_lett = str_1[0]
    str_2_lett = str_2[0]
    
    if ord(str_1_lett) == ord(str_2_lett):
        return (f"Try again! This character's name "
                f"also starts with the letter {str_1_lett}.")
    elif ord(str_1_lett) < ord(str_2_lett):
        return ("Try again! This character's name starts with "
                "a letter that's later in the alphabet.")
    else:
        return ("Try again! This character's name starts with "
                "a letter that's earlier in the alphabet.")    

def guessing_game():
    """
    A game that asks the user to guess the name of a 
    character from The Hobbit or The Lord of the Rings
    """
    
    print("I'm thinking of a character from The Lord of the Rings or "
          "The Hobbit. Can you guess who?")
    
    # randomly choose one of the characters
    i = random.randint(0, len(ls.lotr_characters) - 1)
    character = ls.lotr_characters[i]
    
    guessing = True    
    while guessing is True:            
        # ask the user for their guess
        guess = input("\nCharacter (first name only): ").lower()
        
        # if they're right, congratulate them and end the game    
        if guess == character.first_name:
            print(f"You're right! I'm thinking of {character.get_full_name().title()}.")
            guessing = False

        # if not, tell them whether the first letter in the name is before or after what they guessed
        else:
            game_message = compare_first_letters(guess, character.first_name)
            print(game_message)


def main():
    guessing_game()

if __name__ == '__main__':
    main()

# improvements:
    # increase a counter for each guesses
    # on the fourth guess, ask if the user wants a hint 
    # quit the game if the user's guess is not correct after the hint?