import random

def guessing_game():
    """A game that asks the user to guess a number between 0 and 100"""

    # generate the number that the user will need to guess
    random_num = random.randint(0, 100)

    # a variable to track whether the user needs to keep guessing
    game_running = True
    
    while game_running is True:
        # ask the user to guess the number, and store it as an integer
        user_num = int(input("Guess a number between 0 and 100: "))
            
        # if the user's guess is correct, print a message and exit the program
        if user_num == random_num:
            print(f"Woohoo! You guessed correctly: the number is {random_num}.")
            game_running = False
            
        # otherwise, tell them if their guess is too high or too low
        elif user_num < random_num:
            print(f"The number {user_num} is too low. Try again!")
        else:
            print(f"The number {user_num} is too high. Try again!")

def main():
    guessing_game()

if __name__ == '__main__':
    main()
