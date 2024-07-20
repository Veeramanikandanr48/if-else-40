# Program 1: Even or Odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 2: Larger of Two Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(num1)
else:
    print(num2)

# Program 3: Smallest of Three Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
else:
    print(num3)

# Program 4: Pass or Fail
grade = float(input("Enter the grade percentage: "))
if grade >= 60:
    print("Pass")
else:
    print("Fail")

# Program 5: Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Program 6: Prime or Composite
number = int(input("Enter an integer: "))
if number <= 1:
    print("Composite")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Composite")

# Program 7: Ascending Order of Three Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2

print(num1, num2, num3)

# Program 8: Greatest Common Divisor
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
while b:
    a, b = b, a % b
print(a)

# Program 9: Arithmetic Operations
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation (Add, Subtract, Multiply, Divide): ")

if operation == "Add":
    print(num1 + num2)
elif operation == "Subtract":
    print(num1 - num2)
elif operation == "Multiply":
    print(num1 * num2)
elif operation == "Divide":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

# Program 10: Most Frequent Number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 and num1 == num3:
    print(num1)
elif num1 == num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
elif num1 == num3:
    if num1 > num2:
        print(num1)
    else:
        print(num2)
elif num2 == num3:
    if num2 > num1:
        print(num2)
    else:
        print(num1)
else:
    if num1 < num2 and num1 < num3:
        print(num1)
    elif num2 < num1 and num2 < num3:
        print(num2)
    else:
        print(num3)
