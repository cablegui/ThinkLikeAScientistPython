# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 12:54:56 2017

@author: nevil_000
"""

students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]
    
    
for (name,subjects) in students:
    print("Student ", name, " takes ", len(subjects), " subjects which are ", subjects)