#Create a story
#Author: nmessa
#Date: 10.23.2016
##Reading and writing files demo

#Write first part of story to a file
outfile = open('story.txt', 'w')
outfile.write('Mary had a little lamb\n')
outfile.write('whose fleece was white as snow\n')
outfile.write('and every where that Mary went\n')
outfile.write('the lamb was sure to go.\n')
outfile.close()

#read story from file and display
infile = open('story.txt', 'r')
lines = infile.readlines()
infile.close()
for i in range(len(lines)):
    print (lines[i], end = '')

#Write second part of story to a file
outfile = open('story.txt', 'a')
outfile.write('He followed her to school one day\n')
outfile.write('which broke the teachers rule')
outfile.close()

print ('\n\n\nThe new story')
#read story from file and display
infile = open('story.txt', 'r')
lines = infile.readlines()
infile.close()
for i in range(len(lines)):
    print (lines[i], end = '')
