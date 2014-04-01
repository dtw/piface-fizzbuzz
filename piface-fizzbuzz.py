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

# define a function that does stupid lights with piface
def victoryLights():
    i = 0
    while i<=128:
        pfd.leds[random.randint(0,7)].toggle()
        sleep(0.01)
        i+=1

# turn off all piface lights
def lightsOut():
    # switch out lights
    for led in range(0,7):
        pfd.leds[led].turn_off()


def getPlayerCount():
    count=int(raw_input("How many computer players (between 2 and 4)? ").strip)
    if count >4 or count < 2:
        print("Between 2 and 4!")
        count=getPlayerCount()
    return count

def getAnswer():
    global lives
    # we use lower to make sure case matches
    if raw_input(player + " play!\t").lower().replace(" ", "") != checkFizzbuzz(i).lower():
        # if wrong
        # turn off a light
        pfd.leds[lives-1].turn_off()
        # decrement lives
        lives -= 1
        # print a message
        print("Wrong! " + str(lives) + "/5 lives remaining")
        # if lives left try again
        if lives > 0:
            getAnswer()

def randomiseArray(start_array,no_samples=0):
    # can randomise a whole array or just get random samples
    if no_samples == 0:
        start_array_length = len(start_array)
    else:
        start_array_length = no_samples
    # make a blank array
    return_array = []
    # make a counter
    i = 0
    # loop array length times
    while i < start_array_length:
        # get a random target in the start_array
        target = random.randint(0,len(start_array)-1)
        # add it to the next slot in return_array
        return_array.append(start_array[target])
        # delete it from the start array
        del start_array[target]
        # increment the counter
        i += 1
    # return randomised array
    return(return_array)

# make sure piface lights are off
lightsOut()

# create a list of cpu names
file=open("./cpu_names.txt",'r')
cpu_names=file.read().splitlines()
#cpu_names=file.readline().split()
#cpu_names = ["HAL","WOPR","2501","Jarvis","GERTY"]

# initialise a list of players
player_names = []

# get a name for Player 1
player_name=raw_input("Hi, what's your name Player " + str(len(player_names)) + "? ")
player_names.append(player_name)

# ask how many CPU players
cpu_player_count=getPlayerCount()

# add names to player_names
player_names.extend(randomiseArray(cpu_names,cpu_player_count))

# mix up the players
player_names = randomiseArray(player_names)

# how many turns to play? this is 5 times the number of players so everyone has 5 turns
turns = len(player_names) * 5

# set up 5 lives
global lives
lives = 5

# initialise piface lights
for led in range(0,4):
    pfd.leds[led].turn_on() 
# counter to keep track of answer
i = 1
# turn counter
j = 1

# let's go!
while j<=5:
    for player in player_names:
        # check who's turn it is
        if (player == player_name):
            # it's human player turn so get an answer and check if it is correct
            getAnswer()
            # check if player is out of lives
            if lives == 0:
                break
        else:
            # cpu player turn:
            print(player + " says\t" + checkFizzbuzz(i))
        # increment the answer counter
        i += 1
    # check lives again
    if lives == 0:
        break
    # increment turn counter
    j += 1
# check win conditions!
if lives == 0:
    print("You lose!")
else:
    print("You win!")
    victoryLights()
# switch out piface lights
lightsOut()
