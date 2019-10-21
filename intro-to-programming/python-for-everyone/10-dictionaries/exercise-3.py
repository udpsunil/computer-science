# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have
# come from each email address, and print the dictionary.

file_handle = open(r'/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8'
                   r'-files/mbox-short.txt')
email_count = {}
for line in file_handle:
    line = line.rstrip()
    if line.startswith("From "):
        email = line.split()[1]
        if email not in email_count.keys():
            email_count[email] = 1
        else:
            email_count[email] += 1
print(email_count)
