# Katie Krieger
# 5/7/17

# https://www.rithmschool.com/courses/python-fundamentals-part-1/python-dictionaries-exercises

#1
my_list = [("name", "Elie"), ("job", "Instructor")]
my_dictionary = {my_list[0]:my_list[1] for i in range(0,len(my_list))}

#2
list_1 = ["CA", "NJ", "RI"]
list_2 = ["California", "New Jersey", "Rhose Island"]
my_dictionary = dict(zip(list_1, list_2))
# or {list_2[i]: list_1[i] for i in range(0,3)}

#3
my_dictionary = {char:0 for char in ["a", "e", "i", "o", "u"]}

#4
my_dictionary = {i:chr(i+64) for i in range(1,27)}