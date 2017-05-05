# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:41:51 2017

@author: nevil_000
"""

import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(100)
    tess.left(56)
    wn.ontimer(h1, 2000)

h1()
wn.mainloop()