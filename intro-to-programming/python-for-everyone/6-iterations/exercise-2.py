# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and
# minimum of the numbers instead of the average.


count = 0
total = 0
largest = None
smallest = None
while True:
    try:
        inp = input("Enter a number: ")
        if inp == "done":
            print("Maximum is ",largest)
            print("Minimum is ",smallest)
            break
        else:
            number = int(inp)
            if largest is None: largest = number
            if smallest is None: smallest = number
            largest = max(largest, number)
            smallest = min(smallest, number)
            count += 1;
            total += number
    except:
        print("Invalid input")