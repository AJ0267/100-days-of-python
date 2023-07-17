#Day-9: Dictionaries and nesting

#Dictionaries:

#student dictionary

#keys and values.

students = {
    "name": "Aniket",
    "roll_no": 72,
    "location": "India"
}
print(students["roll_no"])

#Add data

students["hobby"] = "gaming"
print(students)

# empty dictionary

empty_dict = {}

#edit an item in existing dictionary

students["roll_no"] = 26
print(students)

#looping through a dictionary

for key in students:
    # print(key)
    print(students[key])



#coding exercise: grading program

students_scores = {
    "harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 72,
    "Neville" : 62
}

students_grades = {}

for student in students_scores:
    score = students_scores[student]
    if score > 90:
        students_grades[student] = "outstanding"
    elif score > 80:
        students_grades[student] = "exceeds expectations"
    elif score > 70:
        students_grades[student] = "acceptable"
    else:
        students_grades[student] = "failed"
        
print(students_grades)



# nesting

#nest list in a dict.

student = {
    "name" : "aniket",
    "rollno" : 30,
    "skills" : ["python", "html", "css"]
}

#nest a dict in dict

student = {
    "name" : "aniket",
    "rollno" : 45,
    "projects" : {"snake" : ["python", "turtle", "time"]}
}

#nest dict in list

travel_log = [
    {
        "country" : "france",
        "cities_visited" : ["paris", "lille", "dijon"],
        "total_visits" : 12
    },
    {
        "country" : "germany",
        "cities_visited" : ["berlin", "hamburg", "stuttgart"],
        "total_visits" : 12
    }
]





#coding exercise: dict in list.

travel_log = [
    {
        "country" : "france",
        "cities" : ["paris", "lille", "dijon"],
        "total_visits" : 12
    },
    {
        "country" : "germany",
        "cities" : ["berlin", "hamburg", "stuttgart"],
        "total_visits" : 12
    }
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["total_visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


add_new_country("russia", 2 ,["moscow", "Saint petersburg"])
print(travel_log)

