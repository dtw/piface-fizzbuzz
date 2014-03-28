#!/bin/env/python

from time import sleep
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

def victoryLights():
    i = 0
    while i<=128:
        pfd.leds[random.randint(0,7)].toggle()
        sleep(0.01)
        i+=1

def lightsOut():
    # switch out lights
    for led in range(0,7):
        pfd.leds[led].turn_off()

# make sure lights are off
lightsOut()
# create an array of player names
cpu_names = ["HAL","WOPR","2501","Jarvis","GERTY"]
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
lives = 5
# loop through i 1 to 20
while lives > 0:
    current_lives = lives
    while i<=20:
        # check who's turn it is - 3 players take turns, 2 computer players, computer starts
        if (i % player_turn == 0):
            # it's Player 1's turn so get an answer and check if it is correct
            # we use lower to make sure case matches
            if raw_input(player_names[0] + " play! ").lower() != checkFizzbuzz(i).lower():
                # if wrong
                # turn off a light
                pfd.leds[lives-1].turn_off()
                # decrement lives
                lives -= 1
                # print a message
                print("Wrong! " + str(lives) + "/5 lives remaining")
                # we break out without incrementing i so we're still on the same question
                break
            #else:
                # if correct
                #print(checkFizzbuzz(i))
        else:   
            print(checkFizzbuzz(i))
        # increment the counter
        i += 1    
    if (lives == current_lives):
        print("You win!")
        victoryLights()
        break
    if lives == 0:
        print("You lose!")
# switch out lights
lightsOut()
