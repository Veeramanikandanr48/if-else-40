# Program 11: Age Category
age = int(input("Enter age: "))
if age < 18:
    print("Child")
elif 18 <= age <= 65:
    print("Adult")
else:
    print("Senior")

# Program 12: Weight Category
weight = float(input("Enter weight in kilograms: "))
if weight < 18.5:
    print("Underweight")
elif 18.5 <= weight <= 24.9:
    print("Normal weight")
elif 25 <= weight <= 29.9:
    print("Overweight")
else:
    print("Obese")

# Program 13: BMI Category
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

# Program 14: Temperature Check
temperature = float(input("Enter temperature in °C: "))
if temperature >= 37.5:
    print("Fever")
else:
    print("No Fever")

# Program 15: Blood Pressure Category
systolic = int(input("Enter systolic blood pressure: "))
diastolic = int(input("Enter diastolic blood pressure: "))
if systolic < 120 and diastolic < 80:
    print("Normal")
elif 120 <= systolic < 130 and diastolic < 80:
    print("Elevated")
elif (130 <= systolic < 140) or (80 <= diastolic < 90):
    print("Stage 1 Hypertension")
else:
    print("Stage 2 Hypertension")

# Program 16: Tax Bracket
income = float(input("Enter income: "))
taxable_income_threshold = 10000  # Example threshold
middle_income_threshold = 40000  # Example threshold
high_income_threshold = 80000  # Example threshold

if income < taxable_income_threshold:
    print("No Tax")
elif taxable_income_threshold <= income < middle_income_threshold:
    print("Low Tax Bracket")
elif middle_income_threshold <= income < high_income_threshold:
    print("Middle Tax Bracket")
else:
    print("High Tax Bracket")

# Program 17: Retirement Savings Goal
age = int(input("Enter age: "))
income = float(input("Enter income: "))
middle_income_threshold = 40000  # Example threshold
high_income_threshold = 80000  # Example threshold

if age < 18 or age > 65:
    print("No Retirement Savings Needed")
elif income < middle_income_threshold:
    print("Low Retirement Savings Goal")
elif middle_income_threshold <= income < high_income_threshold:
    print("Middle Retirement Savings Goal")
else:
    print("High Retirement Savings Goal")

# Program 18: GPA Status
gpa = float(input("Enter GPA: "))
if gpa < 2.0:
    print("Academic Probation")
else:
    print("Good Standing")

# Program 19: Credit Score Category
credit_score = int(input("Enter credit score: "))
if credit_score < 600:
    print("Poor Credit")
elif 600 <= credit_score <= 699:
    print("Fair Credit")
elif 700 <= credit_score <= 799:
    print("Good Credit")
else:
    print("Excellent Credit")

# Program 20: Work Experience Level
age = int(input("Enter age: "))
years_of_experience = int(input("Enter years of work experience: "))

if age < 25 and years_of_experience < 1:
    print("Entry-level")
elif 25 <= age <= 40 and 1 <= years_of_experience <= 5:
    print("Junior")
elif age > 40 and 5 <= years_of_experience <= 10:
    print("Senior")
elif age > 40 and years_of_experience > 10:
    print("Expert")