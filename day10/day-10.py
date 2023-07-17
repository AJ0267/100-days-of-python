#Functions and Outputs:

# def format_name(f_name, l_name):

#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return  f"Result: {formated_f_name} {formated_l_name}"
# #return = end of function

# print(format_name(input("what is your first name?\n"), input("what is your last name?\n")))


#Docstrings:

def format_name(f_name, l_name):


    """Take a first name and last name and format it to return the title case version of the name."""

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return  f"Result: {formated_f_name} {formated_l_name}"
#return = end of function

print(format_name(input("what is your first name?\n"), input("what is your last name?\n")))

format_name()