# -*- coding: utf-8 -*-
"""
Created on Fri May  5 11:55:25 2017

@author: nevil_000
"""

import mymodule1
import mymodule2

print("My name is", __name__)

print( (mymodule2.myage - mymodule1.myage) ==
       (mymodule2.year - mymodule1.year)  )
       
print((mymodule2.myage - mymodule1.myage))

print((mymodule2.year - mymodule1.year))