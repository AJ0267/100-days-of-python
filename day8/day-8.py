# Day-8 functions 

# def my_func():
#     #do task1
#     #do task2
# def my_func()

# def greet():
#     print("hello")
#     print("howdy?")
#     print("what time?")
# greet()

# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"how you doing {name}?")
# greet_with_name("aniket")

# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")
# greet_with("aniket", "india")
# greet_with(location="india",name="aniket")


#coding challenge: paint area calculator.
# import math
# def paint_calculator(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {num_of_cans} cans of paint.")

# h = int(input("height of wall: \n"))
# w = int(input("width of wall: \n"))
# coverage = 5

# paint_calculator(height=h, width=w, cover=coverage) 


#coding challenge: prime number checker.

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    

n = int(input("enter a number: \n"))

prime_checker(number=n)