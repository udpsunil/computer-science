# Write a program to prompt for a file name, and then read through the file and look for lines of the form
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

mbox_path = input("Enter the file name: ")
file_handle = open(mbox_path)

total_confidence = 0
count = 0
for line in file_handle:
    if line.find('X-DSPAM-Confidence:') != -1:
        total_confidence += float(line.split(':')[1])
        count += 1
print("Average spam confidence: {:.12f}".format(total_confidence/count))