#!/bin/sh
"""
Algorithm :
Enter the names of the files.
Open the first file in append mode and the second file in read mode.
Append the contents of the second file to the first file using the write() function.
"""
import argparse

#Capture the users input for the filenames 
parser = argparse.ArgumentParser(description = "Append content of one text file to another")
parser.add_argument("Firstfile",help= "File to which the contents from otherfile is appended")
parser.add_argument("SecondFile",help= "File from which the contents is read to be append to first file")
args = parser.parse_args()
#Open the files in append mode, read the contents from the second file and append it to first file"
with open(args.SecondFile, 'r') as file2:
    contents=file2.readlines()
    with open(args.Firstfile, 'a') as file1:
        for content in contents:
            file1.write(content)
