#!/bin/env/python

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
        return(i)

# start with a counter i
i=1
# loop through i 1 to 20
while i<20:
    print(checkFizzbuzz(i))
    # increment the counter
    i += 1
