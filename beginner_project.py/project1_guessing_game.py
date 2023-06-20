#user guesses the game,computer selects the random no and keeps it a secret

import random
def guess_user(x):
    guess  = 0 #initialise guess
    no_of_guess =0
    
    random_no = random.randint(1, x) # computer chooses a random no 
    while guess != random_no and no_of_guess < 6:
        guess = int(input('Enter a number between 1 and {x} :'))
        no_of_guess += 1 #incrementing the counts of guesess
        if guess > random_no:
            print('try again, you guessd too high')

        elif guess < random_no:
            print('try again, you guessed too low')
        else: #if guess is equal to the random no
            break

    if guess == random_no:
        print(f'congratulations , {guess} is correct and the count of guesses is {no_of_guess}')
    else:
        print('sorry better luck next time, you are out of guesses')


guess_user(100)
