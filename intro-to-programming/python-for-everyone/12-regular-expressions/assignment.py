import re
print(sum([int(num) for num in re.findall('[0-9]+',open(input("Enter file name: ")).read())]))