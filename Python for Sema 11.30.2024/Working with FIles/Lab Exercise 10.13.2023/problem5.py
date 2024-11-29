#storywriter.py
#Author: nmessa
#Date: 10/13/2023 Problem 5
##This is a program that writes a story to a text file

#get story file name from writer
filename = input("Enter the name of your story: ")
filename += '.txt'

#Enter your story
print('Enter your story.  Enter x to quit')
outfile = open(filename, 'a')
line = ''
while line != 'x':
    line = input()
    if line != 'x':
        outfile.write(line + '\n')
outfile.close()

#read story from file and display
infile = open(filename, 'r')
lines = infile.readlines()
infile.close()
for line in lines:
    print (line, end = '')

