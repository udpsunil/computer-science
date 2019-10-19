# Rewrite your pay compensation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours

try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    extra_pay = 0
    if hours > 40:
        extra_pay = (hours - 40) * rate * 1.5
        pay = 40 * rate
    else:
        pay = hours * rate
    print(f'Pay: {pay+extra_pay}')
except:
    print("Error, please enter numeric input")
