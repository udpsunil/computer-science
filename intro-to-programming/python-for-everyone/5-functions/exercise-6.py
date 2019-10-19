# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes
# two parameters (hours and rate).

def computepay(hours, rate):
    extra_pay = 0
    if hours > 40:
        extra_pay = (hours - 40) * rate * 1.5
        pay = 40 * rate
    else:
        pay = hours * rate
    return pay + extra_pay


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = computepay(hours, rate)
print ("Pay",pay)

