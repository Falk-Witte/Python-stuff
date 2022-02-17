#!bin/python3

#take file as input kinda like in the cat command but way more complicated to execute
i = input("Enter file name=> ")

#open file in readmode
file = open(i, "r")

#read the data from the file
data = file.read()

#print line
print('\n')

#print the data
print(data)

#close the file 
file.close()

#print line
print('\n')