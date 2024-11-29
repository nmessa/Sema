#storywriter.py
#Author: nmessa
#Date: 10.27.2016
##This is a program that writes a story to a text file

#get story file name from writer
filename = input("Enter the name of your story:")
filename += '.txt'

#Enter your story
print("Type your story.  Enter x to quit.")
outfile = open(filename, 'w')
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
for i in range(len(lines)):
    print (lines[i], end = '')
