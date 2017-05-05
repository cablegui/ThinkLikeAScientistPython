# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:42:45 2017

@author: nevil_000
"""

"""
Create a module named wordtools.py with our test scaffolding in place.
Now add functions to these tests pass:
test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
      ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
      ['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now", ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
      ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
      ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
      ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)
Save this module so you can use the tools it contains in future programs.
"""


import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

import string


def cleanword(word):
    j = []
    for i in list(word):
        if i not in string.punctuation:
            j.append(i)
    return "".join(j)

test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") ==  "word")


def has_dashdash(word):
    if '--' in word:
        return True
        

def extract_words(word):
    if has_dashdash(word):
        temp_text = cleanword(word.replace('--',' '))
    else:
        temp_text = cleanword(word.lower())    
        
    return temp_text.split()
    

def wordcount(sub, word):
    counter = 0
    for i in word:
        if sub in i:
            counter += 1
    return counter
    

def wordset(word_list):
    temp_text = list(set(word_list))
    temp_text.sort()
    return temp_text

def longestword(word_list):
    length_word = 0
    for i in word_list:
        if len(i) > length_word:
            length_word = len(i)
    return length_word

