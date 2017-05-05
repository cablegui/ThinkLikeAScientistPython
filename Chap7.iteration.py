# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:48:52 2017

@author: nevil_000
"""

import sys

def test(did_pass):
    """
    Print the result of a test
    """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = ("Test at line {0} is ok".format(linenum))
    else:
        msg = ("Test at line {0} is not ok".format(linenum))
        
    print(msg)
    


def mysum(xs):
    """
    return the sum of all elements in the list xs
    """
    running_total = 0
    for f in xs:
        running_total=running_total + f
        
    return running_total
    

def test_suite():
    test(mysum([1,2,3,4])==10)

test_suite()    
    
    
def myiter(n):
    v = 0
    ss = 0    
    while v <= n:
        print(ss,end=",")
        ss = ss + 1
        v = v + 1
    print(ss,end=".\n")
        
myiter(10)