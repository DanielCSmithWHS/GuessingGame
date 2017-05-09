'''
This is the guessing game!
Created by Daniel Smith
contact@danielsmith.co
Created to play around with Python
Py2
'''

# Import required modules
import math
from time import *
from random import *

# Foundations
gameMode = 0
roundsPlayed = 0
mitchelNumber = 0
playerName = ""



def mode():
    global gameMode
    global mitchelNumber
    gameMode = randint(1,2)
    if gameMode == 1:
        mitchelNumber = randint(1,10)
    elif gameMode == 2:
        mitchelNumber = randint(1,100)
    # gameMode 3 is currently disabled, this is because 1000 seemed too high in it's current text based game mode
    # note for future use: possible for other guessing games, like what am I thinking?
    elif gameMode == 3:
        mitchelNumber = randint(1,1000)
    story()

def story():
    global playerName
    global roundsPlayed
    if roundsPlayed == 0:
        print('Welcome to the GuessingGame!')
        sleep(0)
        playerName = input("What is your name?")
        sleep(1)
        print("Hello {}, my name is Mitchel.".format(playerName))
        sleep(1)
        print("This place is still under construction, I'm sure I can get 3D working....")
        sleep(2)
        print('But enough of that.')
        sleep(1)
    else:
        print("")
        print("")
        print("Welcome back",playerName,"!")
    global gameMode
    if gameMode == 1:
        print("This round will be a number between 1 and 10")
    elif gameMode == 2:
        print("This round will be a number between 1 and 100")
    elif gameMode == 3:
        print("This round will be a number between 1 and 1000")
    sleep(2)
    print("")
    input("Press Enter to continue...")
    guess()


def guess():
    try:
        myGuess = int(input("What is my number?"))
    except ValueError:
        print("Please put a number")
        sleep(1)
        print("Lets try this again.... -_-")
        sleep(2)
        guess()
    global mitchelNumber
    global roundsPlayed
    if myGuess == mitchelNumber:
        print("That is right! {} was my number!".format(mitchelNumber))
        sleep(2)
        restart = input("Wanna play again? Y/N").upper()
        if restart == "Y":
            roundsPlayed += 1
            mode()
        if restart == "N":
            print("Thanks for playing!")
            return()
    elif myGuess > mitchelNumber:
        print("That's too high")
        guess()
    elif myGuess < mitchelNumber:
        print ("That's too low")
        guess()
mode()

'''
This concludes the game. The project will continue under a different direction.
Py3 will contain a window, that will play the same game.
Py4 will probably also be window based, but will use a different game style (20 questions?)
Py4 will look graphically better, as Py3 is purely a test of GUIs, not of the code base. 
Expect Py3 to have identical code, and Py4 to have a similar code base. 
'''



