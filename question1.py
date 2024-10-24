# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")


# Question 1(ii)
# Write a Python program to find maximum between three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
max_number = max(num1, num2, num3)
print(f"The maximum number between {num1}, {num2}, and {num3} is: {max_number}")

