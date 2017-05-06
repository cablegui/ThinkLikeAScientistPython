# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:56:57 2017

@author: nevil_000
"""
#########################################
myfile = open("test.txt", "w")

myfile.write("Hello there\n")
myfile.write("Daisy and Poppy")
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

print(xs)

words = xs.split()

print(words)

########################################

# Remove lines beginning with #
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
     
"""     
Write a program that reads a file and writes out a new file with the lines in reversed order 
(i.e. the first line in the old file becomes the last one in the new file.)
   
"""


old_file = open("test.txt", "r")
new_file = open("new_test.txt","w")

old_file_list = old_file.readlines()
old_file.close()

old_file_list.reverse()

new_file.writelines(old_file_list)
new_file.close()


"""
Write a program that reads a file and prints only those lines that contain the substring snake.

"""

file_handle = open("snake_text.txt", "r")

while True:
    line_read = file_handle.readline()
    if len(line_read) == 0:
        break
    
    if 'snake' in line_read:
        print(line_read)
    
file_handle.close()

"""
Write a program that reads a text file and produces an output file which is a copy of the file, 
except the first five columns of each line contain a four digit line number, 
followed by a space. Start numbering the first line in the output file at 1. 
Ensure that every line number is formatted to the same width in the output file. 
Use one of your Python programs as test data for this exercise: your output should be a 
printed and numbered listing of the Python program.
"""

file_handle = open("snake_text.txt", "r")
file_handle2 = open("snake_text_numbered.txt", "w")

layout = "{0:>4}, ' ' , {1}"

i = 1
while True:
    line_read = file_handle.readline()
    if len(line_read) == 0:
        break
    file_handle2.write(str(i).zfill(4) + ' ' + line_read)
    i += 1
       
    
file_handle.close()
file_handle2.close()

"""
Write a program that undoes the numbering of the previous exercise: 
it should read a file with numbered lines and produce another file without line numbers.
"""

file_handle = open("snake_text_numbered.txt", "r")
file_handle2 = open("snake_text_no_numbered.txt", "w")

layout = "{0:>4}, ' ' , {1}"


while True:
    line_read = file_handle.readline()
    if len(line_read) == 0:
        break
    file_handle2.write(line_read[5:])
    
       
    
file_handle.close()
file_handle2.close()
