# Day-5 loops in python

fruits = ["fruit1", "fruit2", "fruit3"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")



#coding exercise: average height.

student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0

for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(average_height)


#coding challenge: highest score.

student_scores = input("Input a list of student scores.\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is : {highest_score}!")



#for loops and the range function:

for number in range(1, 10):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)




#coding challenge: adding even numbers.

total = 0
for n in range(2, 101, 2):
    total += n
print(total)



#coding challenge: adding even numbers.

total = 0
for n in range(1, 101, 2):
    print(n)
    total += n
print(total)