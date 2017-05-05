# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 22:23:52 2017

@author: nevil_000
"""

import random

# Create a black box object that generates random numbers
rng = random.Random(123) # With known starting state

dice_throw = rng.randrange(1,7)   # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0

delay_in_seconds

rng.randrange(1,100,3)


cards = list(range(52))  # Generate ints [0 .. 51]
                         #    representing a pack of cards.

cards
rng.shuffle(cards)       # Shuffle the pack
cards

############################################################

import random

def make_random_ints_no_dups(num, lower_bound, upper_bound):
   """
     Generate a list containing num random ints between
     lower_bound and upper_bound. upper_bound is an open bound.
     The result list cannot contain duplicates.
   """
   result = []
   rng = random.Random()
   for i in range(num):
        while True:
            candidate = rng.randrange(lower_bound, upper_bound)
            if candidate not in result:
                break
        result.append(candidate)
   return result

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)


xs = make_random_ints_no_dups(10, 1, 6)
print(xs)

############################################################