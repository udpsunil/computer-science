# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message. If the score is
# between 0.0 and 1.0, print a grade

try:
    score = float(input("Enter score: "))
    if 0.0 <= score <= 1.0:
        grade = ""
        if score >= 0.9:
            grade = "A"
        elif score >= 0.8:
            grade = "B"
        elif score >= 0.7:
            grade = "C"
        elif score >= 0.6:
            grade = "D"
        else:
            grade = "F"
        print(grade)
    else:
        raise Exception
except:
    print("Bad score")
