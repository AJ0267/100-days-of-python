#create list using list comprehension 

# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# >>>> [2, 3, 4]

# name = "aniket"
# letters_list = [letter for letter in name]
# print(letters_list)


#conditional list comprehension

# new_list = [new_item for item in list if test]
 


#coding exercise: squaring numbers
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n**2 for n in numbers]
# print(squared_numbers)

#coding exercise: finding even
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# even_numbers = [n for n in numbers if n % 2 == 0]
# print(even_numbers)

#coding exercise: data overlap
# with open("file1.txt") as file_1:
#     file_1_data = file_1.readlines()

# with open("file2.txt") as file_2:
#     file_2_data = file_2.readlines()

# result = [int(num) for num in file_1_data if num in file_2_data]
# print(result)


#dict comprehension
# dict = { 
#     new_key: new_value for n in list/dict
# }

# import random
# names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']
# student_scores = {
#     student: random.randint(1, 100) for student in names
# }
# print(student_scores)
# passed_students = {
#     student:score  for (student, score) in student_scores.items() if score > 60 
# }
# print(passed_students)


#coding exercise: 
# sentence = "what it the airspeed velocity of an unladen swallow"
# result = {
#     word:len(word) for word in sentence.split()
# }
# print(result)

#coding exercise: 
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {
#     day: (temp * 9/5) + 32   for day, temp in weather_c.items()
# }

# print(weather_f)

student_dict = {
    "student": ["aniket", "harshad", "goku"],
    "score" : [55, 75, 98]
}

# for (key, value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame
(student_dict)
# print(student_data_frame)

