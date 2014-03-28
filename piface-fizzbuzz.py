#!/bin/env/python

import pifacedigitalio
import random

pfd = pifacedigitalio.PiFaceDigital()


# define a function that checks for Fizzbuzz
def checkFizzbuzz(i):
    # if i can be divided exactly by 5
    if (i % 5 == 0):
        # can it also be divided by 2
        if (i % 2 == 0):
            # Fizzbuzz
            return("Fizzbuzz")
        else:
            # if not then just Buzz
            return("Buzz")
    # can i be divided by 2
    elif (i % 2 == 0):
        # then Fizz
        return("Fizz")
    else:
        #otherwise just return i
        return(str(i))

# create an array of player names
player_names = []
# get a name for Player 1
player_names.append(raw_input("Hi, what's your name Player " + str(len(player_names)) + "? "))
# since don't want the player to have the same turn everytime so
player_turn = random.randint(2,3)
# make a variable to check for a loss
player_lost = False
# start with a counter i
i=1
# set up 5 lives
for led in range(0,7):
    if led < 5:
        pfd.leds[led].turn_on()
    else:
        pfd.leds[led].turn_off()
lives = 5
# loop through i 1 to 20
while lives > 0:
    while i<=10:
        # check who's turn it is - 3 players take turns, 2 computer players, computer starts
        if (i % player_turn == 0):
            # it's Player 1's turn so get an answer and check if it is correct
            # we use lower to make sure case matches
            if raw_input(player_names[0] + " play! ").lower() != checkFizzbuzz(i).lower():
                # if wrong
                print("Wrong!")
                pfd.leds[lives-1].turn_off()
                lives -= 1
                break
            #else:
                # if correct
                #print(checkFizzbuzz(i))
        else:   
            print(checkFizzbuzz(i))
        # increment the counter
        i += 1
if (player_lost == False):
    print("You win!")
# switch out lights
for led in range(0,7):
    pfd.leds[led].turn_off()
