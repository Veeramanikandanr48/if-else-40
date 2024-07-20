# Program 1: Maximum between Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Maximum is:", num1)
else:
    print("Maximum is:", num2)

# Program 2: Maximum between Three Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Maximum is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maximum is:", num2)
else:
    print("Maximum is:", num3)

# Program 3: Check Whether a Number is Negative, Positive, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Program 4: Check Whether a Number is Divisible by 5 and 11
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")

# Program 5: Check Whether a Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Program 6: Check Whether a Year is a Leap Year or Not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Program 7: Check Whether a Character is an Alphabet or Not
char = input("Enter a character: ")
if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print("Alphabet")
else:
    print("Not an Alphabet")

# Program 8: Check Whether an Alphabet is a Vowel or Consonant
char = input("Enter an alphabet: ").lower()
if char in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")

# Program 9: Check Whether a Character is an Alphabet, Digit, or Special Character
char = input("Enter a character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")

# Program 10: Check Whether a Character is Uppercase or Lowercase Alphabet
char = input("Enter a character: ")
if char.isalpha():
    if char.isupper():
        print("Uppercase Alphabet")
    else:
        print("Lowercase Alphabet")
else:
    print("Not an Alphabet")

# Program 11: Print Weekday from Week Number
week_number = int(input("Enter week number (1-7): "))
if week_number == 1:
    print("Monday")
elif week_number == 2:
    print("Tuesday")
elif week_number == 3:
    print("Wednesday")
elif week_number == 4:
    print("Thursday")
elif week_number == 5:
    print("Friday")
elif week_number == 6:
    print("Saturday")
elif week_number == 7:
    print("Sunday")
else:
    print("Invalid week number")

# Program 12: Print Number of Days in a Month
month_number = int(input("Enter month number (1-12): "))
if month_number in [1, 3, 5, 7, 8, 10, 12]:
    print("31 days")
elif month_number in [4, 6, 9, 11]:
    print("30 days")
elif month_number == 2:
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days")
    else:
        print("28 days")
else:
    print("Invalid month number")

# Program 13: Count Total Number of Notes in Given Amount
amount = int(input("Enter amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

for note in notes:
    total_notes += amount // note
    amount %= note

print("Total number of notes:", total_notes)

# Program 14: Check Whether Triangle is Valid Based on Angles
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))
if angle1 + angle2 + angle3 == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# Program 15: Check Whether Triangle is Valid Based on Sides
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Valid Triangle")
else:
    print("Invalid Triangle")

# Program 16: Check the Type of Triangle (Equilateral, Isosceles, or Scalene)
side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))
if side1 == side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Program 17: Find All Roots of a Quadratic Equation
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Two distinct real roots:", root1, "and", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("One real root:", root)
else:
    print("No real roots")

# Program 18: Calculate Profit or Loss
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))
if selling_price > cost_price:
    print("Profit:", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss:", cost_price - selling_price)
else:
    print("No Profit No Loss")

# Program 19: Calculate Percentage and Grade
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))
biology = float(input("Enter marks in Biology: "))
mathematics = float(input("Enter marks in Mathematics: "))
computer = float(input("Enter marks in Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")

# Program 20: Calculate Gross Salary
basic_salary = float(input("Enter basic salary: "))
if basic_salary <= 10000:
    hra = basic_salary * 0.20
    da = basic_salary * 0.80
elif basic_salary <= 20000:
    hra = basic_salary * 0.25
    da = basic_salary * 0.90
else:
    hra = basic_salary * 0.30
    da = basic_salary * 0.95

gross_salary = basic_salary + hra + da
print("Gross Salary:", gross_salary)

# Program 21: Calculate Total Electricity Bill
units = float(input("Enter electricity units: "))
bill = 0

if units <= 50:
    bill = units * 0.50
elif units <= 150:
    bill = (50 * 0.50) + ((units - 50) * 0.75)
elif units <= 250:
    bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
else:
    bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)

surcharge = bill * 0.20
total_bill = bill + surcharge
print("Total Electricity Bill:", total_bill)
