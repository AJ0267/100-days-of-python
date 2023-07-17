#file not found
# with open("data.txt") as data_file:
#     data_file.read()

#key error
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existent_key"]

#index error
# fruit_list = ["apple", "peach", "grapes"]
# fruit = fruit_list[3]

#type error
# text = "abc"
# print(text + 1)

#exception handling:
# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens


#index error handling:
# fruits = ["apple", "pear", "banana"]
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit Pie")
#     else:
#         print(fruit + " pie")

# make_pie(1)

#key error handling:
# facebook_posts = [
#     {'Likes' : 21, 'Comments' : 2},
#     {'Likes' : 13, 'Comments' : 2, 'Shares' : 1},
#     {'Likes' : 33, 'Comments' : 8, 'Shares' : 3},
#     {'Comments' : 4, 'Shares': 2},
#     {'Comments' : 1, 'Shares': 1},
#     {'Likes' : 19, 'Comments' : 3},
# ]
# total_likes = 0s
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
# print(total_likes)