#read 

with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#write

with open("my_file.txt", mode= "w") as file: #if file doesnt exist then automatically create new one
    file.write("your text")  #use \n before text to add to the new line

