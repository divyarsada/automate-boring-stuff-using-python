#!/bin/sh

import argparse

parser = argparse.ArgumentParser(description = "Python Program to Reverse the Content of a File using Stack")
parser.add_argument("Outputfile",help = "Output file")
parser.add_argument("Inputfile", help = "Input file")
args = parser.parse_args()
#print(args)

# Creating Stack class (LIFO rule)
class Stack:

    def __init__(self):

        # Creating an empty stack
        self._arr = []

    # Creating push() method.
    def push(self, val):
        self._arr.append(val)

    def is_empty(self):

        # Returns True if empty
        return len(self._arr) == 0

    # Creating Pop method.
    def pop(self):

        if self.is_empty():
            print("Stack is empty")
            return

        return self._arr.pop()
# Creating a function which will reverse the lines of a file and Overwrites the  given file with its contents line-by-line 
# reversed 

def reverse_file(inputFile,outputFile):
    s= Stack()
    with open(inputFile,'r') as infile:
        for line in infile:
            s.push(line)
    print(s)
    with open(outputFile,'w') as outfile:
        while not s.is_empty():
            outfile.write(s.pop())

reverse_file(args.Inputfile,args.Outputfile)

#Reading the output file and display the contents
with open(args.Outputfile, 'r') as outfile:
    for line in outfile:
        print(line.strip('\n'))
