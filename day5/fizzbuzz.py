#Day-5 interview question: Fizzbuzz

# if number is divisible by 3 then print fizz
# if number is divisible by 5 then print buzz
# if number is divisible by both 3 and 5 then print fizzbuzz

for number in range(1, 101):
    if number % 3 == 0  and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

