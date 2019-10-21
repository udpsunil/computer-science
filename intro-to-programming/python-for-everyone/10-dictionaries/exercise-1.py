# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. Then you can use the in operator as a fast way to 
# check whether a string is in the dictionary.
import string

file_handle = open(r'./words.txt')
words_d = {}
for line in file_handle:
    line = line.rstrip()
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in words_d.keys():
            words_d[word] = 1
        else:
            words_d[word] += 1
print(words_d)
