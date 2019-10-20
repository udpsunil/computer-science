# Write a program to open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function. For each word,
# check to see if the word is already in a list. If the word is not in the list,
# add it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.

file_path = r"/home/sunil/OpenSource/Learning/computer-science/intro-to-programming/python-for-everyone/9-lists/romeo.txt"
file_handle = open(file_path)
word_list = []
for line in file_handle:
    words = line.rstrip().split()
    for word in words:
        if word not in word_list:
            word_list.append(word)
word_list.sort()
print(word_list)
