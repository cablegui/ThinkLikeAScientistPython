# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:56:57 2017

@author: nevil_000
"""
#########################################
myfile = open("test.txt", "w")

myfile.write("Hello there")
myfile.close()

#########################################
mynewhandle = open("test.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()
#########################################


myhandle = open("test.txt","r")

xs = myhandle.readlines()

print(xs)
myhandle.close()

########################################

myhandle = open("test.txt","r")
xs = myhandle.read()
myhandle.close()

words = xs.split()

print(words)

########################################


 def filter(oldfile, newfile):
     infile = open(oldfile, "r")
     outfile = open(newfile, "w")
     while True:
         text = infile.readline()
         if len(text) == 0:
            break
         if text[0] == "#":
            continue

         # Put any more processing logic here
         outfile.write(text)

     infile.close()
     outfile.close()
#######################################
     
# Fetching data from the web

import urllib.request

url = "http://xml.resource.org/public/rfc/txt/rfc793.txt"
destination_filename = "rfc793.txt"

urllib.request.urlretrieve(url, destination_filename)

#########################################################

import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.readall())
    my_socket.close()
    return dta

the_text = retrieve_page("http://xml.resource.org/public/rfc/txt/rfc793.txt")
print(the_text)

#######################################################
     
     