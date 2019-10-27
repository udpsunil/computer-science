# Write a program to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of
# the numbers and print out the average as an integer.
import re

file_path = input("Enter file: ")
file_handle = open(file_path)
lst = []
for line in file_handle:
    line = line.rstrip()
    l = re.findall('New Revision: \d\d\d\d\d', line)
    if len(l):
        lst+=l
print(int(sum([float(string.split(':')[1]) for string in lst])/len(lst)))