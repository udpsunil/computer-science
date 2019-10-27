# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular
# expression and count the number of lines that matched the regular expression
import re

regex = input("Enter a regular expression: ")
mbox_path = r'/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8-files/mbox' \
            r'.txt '

match_count = 0
file_handle = open(mbox_path)
for line in file_handle:
    line = line.rstrip()
    x = re.findall(regex, line)
    match_count += len(x)
print('mbox.txt had {} lines that matched {}'.format(match_count, regex))
