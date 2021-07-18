import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid type")
    sys.exit(1)

try:
    result = x/y
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

#print(x/y)