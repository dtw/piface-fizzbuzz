#!/bin/env/python
# start with a counter i
i=1
# loop through i 1 to 20
while i<20:
    # if i can be divided exactly by 5
    if (i % 5 == 0):
        # can it also be divided by 2
        if (i % 2 == 0):
            # Fizzbuzz
            print("Fizzbuzz")
        else:
            # if not then just Buzz
            print("Buzz")
    # can i be divided by 2
    elif (i % 2 == 0):
        # then Fizz
        print("Fizz")
    else:
        #otherwise just print i
        print(i)
    # increment the counter
    i += 1
