# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 13:00:19 2017

@author: nevil_000
"""

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    counter = 0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.00001:            
            return better
        counter += 1
        print("Counter at ", counter)
        approx = better

# Test cases
print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))