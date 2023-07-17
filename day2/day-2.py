#Day-2 : python primitive data types, Type error, type checking and type conversion, mathematical operations.
#number manipulation and F strings


# coding challenge: BMI calculator.

height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)



#coding challenge: life in weeks.

age = input("what is your age?\n")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")
