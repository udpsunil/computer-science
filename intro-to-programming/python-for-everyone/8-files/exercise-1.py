# Write a program to read through a file and print the contents of the file (line by line) all
# in upper case. Executing the program will look as follows

file_handle = open('/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8-files/mbox-short.txt')
for line in file_handle:
    print(line.upper(),end="")