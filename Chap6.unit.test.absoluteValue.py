# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:32:04 2017

@author: nevil_000
"""

import sys

def test(did_pass):
    """
    Print the result of a test
    """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} is ok".format(linenum)
    else:
        msg = "Test at line {0} is not ok".format(linenum)
        
    print(msg)
    
    
    
def test_suite():
    test(absolute_value(17)==17)
    test(absolute_value(-17)==17)
    test(absolute_value(0)==0)
    test(absolute_value(3.14)==3.14)
    test(absolute_value(-3.14)==3.14)
    

def absolute_value(val):
    if val <= 0:
        return abs(val)
    else:
        return val


test_suite()
    