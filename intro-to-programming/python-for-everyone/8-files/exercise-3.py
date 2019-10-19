# Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter
# Egg to their program. Modify the program that prompts the user for the file name so that it
# prints a funny message when the user types in the exact file name "na na boo boo".
# The program should behave normally for all other files which exist and don't exist.

mbox_path = input("Enter the file name: ")
try:
    file_handle = open(mbox_path)
    total_subjects = 0
    for line in file_handle:
        if line.startswith("Subject:"):
            total_subjects += 1
    print("There were {} subject lines in {}".format(total_subjects, mbox_path))
except:
    if mbox_path == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File cannot be opened: {}".format(mbox_path))