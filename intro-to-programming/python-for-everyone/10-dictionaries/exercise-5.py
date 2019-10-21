# This program records the domain name (instead of the address) where the message was sent from instead of who the
# mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

file_handle = open(r'/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8'
                   r'-files/mbox-short.txt')
domain_count = {}
for line in file_handle:
    line = line.rstrip()
    if line.startswith("From "):
        email = line.split()[1]
        domain = email.split('@')[1]
        if domain not in domain_count.keys():
            domain_count[domain] = 1
        else:
            domain_count[domain] += 1
print(domain_count)
