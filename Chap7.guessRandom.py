# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 19:37:09 2017

@author: nevil_000
"""

import random

rng = random.Random()

number = rng.randrange(1,1000)

guesses = 0
msg=""

while True:
    guess = int(input(msg + "\nGuess my number between 1 and 1000\n"))
    guesses += 1
    if guess < number:
        msg += str(guess) + " is too low\n"
    elif guess > number:
        msg += str(guess) + " is too high\n"
    else:
        break

input("\n\nGreat you got it in {0} tries".format(guesses))