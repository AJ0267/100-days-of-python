#Day-4: random module, python lists

import random
random_integer = random.randint(1, 10)
print(random_integer)
random_float = random.random() * 5
print(random_float)




#coding challenge: Heads or Tails.

import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else: 
    print("Tails")


fruits = ["fruit1", "fruit2", "fruit3"] #0 1 2    -3 -2 -1
print(fruits[2])
print(fruits[-2])

fruits.append("fruits4")
print(fruits)

fruits.extend(["fruit5", "fruit6", "fruit7"])
print(fruits)




#coding challenge: Who will pay the bill?

import random
names_string = input("Give the everybody's names, separated by a comma.\n")
names = names_string.split(", ")
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to pay for the meal today!")


dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "potatoes"]
fruits = ["strawberries", "Nectrines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)




#coding challenge: Treasure map.

row1 = ["🗿", "🗿", "🗿"]
row2 = ["🗿", "🗿", "🗿"]
row3 = ["🗿", "🗿", "🗿"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")