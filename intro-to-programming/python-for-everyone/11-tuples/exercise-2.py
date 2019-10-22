# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from
# the "From" line by finding the time string and then splitting that string into parts using the colon character.
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown
# below.

file_handle = open(r'/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/8'
                   r'-files/mbox-short.txt')
hour_count = {}
for line in file_handle:
    line = line.rstrip()
    if line.startswith("From "):
        hour = line.split()[5].split(':')[0]
        if hour not in hour_count.keys():
            hour_count[hour] = 1
        else:
            hour_count[hour] += 1

hour_list = []
for key, value in hour_count.items():
    hour_list.append((key, value))

hour_list.sort()

for hour, count in hour_list:
    print(hour, count)


