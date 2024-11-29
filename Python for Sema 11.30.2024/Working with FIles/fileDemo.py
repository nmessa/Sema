#File Demo
#Author nmessa

#Open a file for writing
outFile = open('test.txt', 'w')
bookTitle = "This is It"
author = "Alan Watts"
outFile.write(bookTitle + '\n')
outFile.write(author)
outFile.close()

#Read from a file and store in a list
inFile = open('test.txt', 'r')
lines = inFile.readlines()
inFile.close()

#Output the file contents as a list
print ("Lines = " + str(lines))
print()
print()
#Output each element of the list
print( "The contents of the test file:")
for i in range(len(lines)):
    print ('\t', lines[i],)

##Sample Output:
##Lines = ['This is It\n', 'Alan Watts']
##
##
##The contents of the test file:
##	This is It
##	Alan Watts
