# Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line.
# Count the number of messages from each person using a dictionary.
#
# After all the data has been read, print the person with the most commits by creating a list of (count,
# email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most
# commits.
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

email_list = []
for key, value in email_count.items():
    email_list.append((value, key))

email_list.sort(reverse=True)
print(email_list[0][1], email_list[0][0])
