# Write a program that categorizes each mail message by which day of the week the commit was 
# done. To do this look for lines that start with "From", then look for the third word and keep
# a running count of each of the days of the week. At the end of the program print out the
# contents of your dictionary (order does not matter).

file_handle = open(r'/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8'
                   r'-files/mbox-short.txt')
days_count = {}
for line in file_handle:
    line = line.rstrip()
    if line.startswith("From "):
        day = line.split()[2]
        if day not in days_count.keys():
            days_count[day] = 1
        else:
            days_count[day] += 1
print(days_count)
