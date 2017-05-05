# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 07:32:08 2017

@author: nevil_000
"""

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

wn.bgcolor("lightgreen")
alex.shape("turtle")

alex.penup()
for i in range(30):
    alex.stamp()
    alex.forward(20 + i)
    alex.right(30)

alex.color("blue")

alex.write("Hello there")
wn.exitonclick()