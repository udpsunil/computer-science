# Add code to the above program to figure out who has the most messages in the file. After all the data has been read
# and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and
# minimum loops) to find who has the most messages and print how many messages the person has.

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
most = max(email_count.values())
for key, value in email_count.items():
    if value == most:
        print("{} {}".format(key, most))
