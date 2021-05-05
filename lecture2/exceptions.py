import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input. Must be number.")
    sys.exit(1) # something went wrong

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Can't divide by 0.")
    sys.exit(1)

print(f"{x} / {y} is {result}")