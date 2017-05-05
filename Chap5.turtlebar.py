# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 12:59:24 2017

@author: nevil_000
"""

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue","red") # draw line of color blue and fill with red
tess.penup()
tess.setx(-200)
tess.pendown()

xs = [48,117,200,240, 160, 260, 220]


def draw_bar(t,height):
    """Get Turtle to draw one bar of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(" " + str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()
    
    
for v in xs:
    draw_bar(tess,v)

wn.exitonclick() # Exit the window and then say turtle.done()
turtle.done()