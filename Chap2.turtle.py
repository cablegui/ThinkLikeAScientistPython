# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 06:39:30 2017

@author: nevil_000
"""

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)
    alex.forward(50)

wn.exitonclick()
