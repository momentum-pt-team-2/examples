import random


def guess_number(number, you_won):    
    print("The number is: ", number)
    guess = int(input("Guess a number between 1 and 20: "))
    print(guess)

    if guess > number:
        print("That's too high!")
    elif guess < number:
        print("That's too low!")
    else:
        print("You're right!")
        you_won = True

    return guess, you_won

def play_game():
    you_won = False
    lives = 5
    guesses = []
    number_to_guess = random.randint(1, 20)
    while you_won == False and lives > 0:
        guess, you_won = guess_number(number_to_guess, you_won)
        if not you_won:
            lives -= 1
            guesses.append(guess)
            # print("You have guessed: ")
            # for number in guesses:
            #     print(number)
            # three above lines are equivalent to the line below
            print('The numbers you have guessed are: ',",".join(f"{number}" for number in guesses))

    if lives == 0:
        print("You ran out of guesses!")
    elif you_won:
        print("You won!")

play_game()