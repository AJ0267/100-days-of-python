#Day-3: 
#  if/else and conditional operators

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))
if height >= 120:
    print("You can ride this rollercoaster!")
else:
    print("sorry, you have to grow taller before you can ride.")



#code challenge: odd or even excercise

number = int(input("Which number do you want to check?\n"))
if number % 2 == 0:
    print("The given number is even.")
else:
    print("The given number is an odd.")





# if/elif conditions and nested if statements:

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))
age = int(input("what is your age?\n"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")

    if age < 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay, have a free ride!")
    else:
        bill = 12
        print("adult tickets are $12.")


    photo = input("Do you want a photo taken? Y Or N.\n")
    if photo == "Y":
        bill += 3
    
    print(f"Your final bill is ${bill}.")

else:
    print("Sorry, You have to grow taller before you can ride.")






#coding challenge: Pizza order.


print("welcome to Pizza Deliveries!")
size  = input("what size do you want? S, M, L\n")
add_pepperoni = input("Do you want to add pepperoni? Y or N\n")
extra_cheese = input("Do you want extra cheese? Y or N\n")

bill = 0 

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else: 
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"your final bill is ${bill}.")


