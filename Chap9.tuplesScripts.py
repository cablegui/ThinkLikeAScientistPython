# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 20:30:42 2017

@author: nevil_000
"""

def f(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
    
f(2.5)

