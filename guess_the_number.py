# Joanna Folk
# 07/29/2019
# guess_the_number
# a game in which the player guesses a randomly generated number

import random

# assign global variables
userNumber = 0
roundsPlayed = 0

# to get user name
userName = input('Hello!  What is your name? ')
print()

# to explain the logic of the game with emphasis on inputs
print('Well ' + userName.title() + ', I am thinking of a number between 1 and 20.')
print('You can ask for a hint by typing \'hint\' or type \'exit\' if you\'re done playing.')

# create the random number the player must guess
computerNumber = random.randint(1, 20)

# to begin the loop which allows endless plays
while userNumber != computerNumber:
    print()
    userNumber = input('Take a guess: ')
    roundsPlayed += 1

    # to create an exit situation with option to play another match
    if userNumber.lower() == 'exit':
        print('You played a good game! The number I chose was: ' + str(computerNumber))
        playAgain = input('Would you like to play another match? (y/n)')
        playAgain = playAgain.lower() # to help with case match

        # for yes to play another game
        if playAgain == 'y' or playAgain == 'yes':
            print()
            print('Alright, let\'s play another game:\nI\'m thinking of a number between 1 and 20.')
            roundsPlayed = 0 # to reset variables
            computerNumber = random.randint(1, 20)

        # otherwise to end the game
        elif playAgain != ('y', 'yes'):
            print('Thanks for playing!')
            exit()

    elif userNumber.lower() == 'hint':
        hintHelp = input('Alright, are you sure you want a hint?: (y/n)')

        if hintHelp.lower() == 'y' or hintHelp.lower() == 'yes':
            hintType = input('Well then, a big hint or a little?: ')

            if hintType.lower() == 'little':
                print('Okay, here\'s your little hint.')

                if computerNumber >= 10:
                    print('The number is in the double digits')

                if computerNumber < 10:
                    print('The number is in the single digits')

            if hintType.lower() == 'big':
                print('Okay, here\'s your big hint.')

                if computerNumber < 6:
                    print('The number is somewhere below five.')

                elif computerNumber > 4 and computerNumber < 11:
                    print('The number is somewhere between 5 and 10.')

                elif computerNumber > 9 and computerNumber < 16:
                    print('The number is somewhere between 10 and 15.')

                elif computerNumber >= 15:
                    print('The number is somewhere between 15 and 20.')

        else:
            print('Let\'s get back to it!\nI\'m thinking of a number between 1 and 20.')


    # to cover bases if user inputs number too high or too low
    elif (int(userNumber) <= 0) or (int(userNumber) >= 21):
        print('Cheeky!  I said guess a number between 1 and 20.  Try again!')

    # if number guessed is lower than the computer number
    elif int(userNumber) < computerNumber:
        print('\033[1m{}\033[0m'.format(userNumber) + ' is too low.  Try again.')

    # if the number guessed is higher than the computer number
    elif int(userNumber) > computerNumber:
        print('\033[1m{}\033[0m'.format(userNumber) + ' is too high. Try again.')

    # if the number guessed is identical to the computer number
    else:
        print('Great job ' + userName.title() + '!  You guessed my number in ' + str(roundsPlayed) + ' round(s)!')
        anotherRound = input('Would you like to play another match? (y/n): ') # to play another round

        # if yes then the game restarts
        if anotherRound.lower() == 'y' or anotherRound.lower() == 'yes':
            print('\nAlright, let\'s go!  I\'m thinking of another number between 1 and 20.')
            print('Don\'t forget you can always type \'exit\' or \'hint\' if you\'re stuck.')
            roundsPlayed = 0 # to reset variables
            computerNumber = random.randint(1, 20)

        else: # otherwise everything ends
            print('Let\'s play again soon.  Have a good day!')
            exit()
