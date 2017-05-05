# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 22:27:09 2017

@author: nevil_000
"""

import string

alphabet = string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}

for x in sentence:
    if x in alphabet:
        if x in count_letters:
            count_letters[x] += 1
        else:
            count_letters[x] = 1
        
        
        
count_letters


#OR##

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

sentence = sentence.replace(' ', '')

count_letters = {}
for x in sentence:
    count_letters[x] = sentence.count(x)
    
    

##################################################
    
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

sentence = sentence.replace(' ', '')

# Create your function here!
def counter(sent):
    count_letters = {}
    for x in sent:
        count_letters[x] = sent.count(x)
        
    return count_letters

counter(sentence)

##################################################





