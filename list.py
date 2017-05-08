# Katie Krieger
# 5/7/17

# https://www.rithmschool.com/courses/python-fundamentals-part-1/python-lists-exercise

# Part 1

#1
list = [1,2,3,4]
[print(num) for num in list]

#2
[print(num*20) for num in list]

#3
list = ["Elie", "Tim", "Matt"]
new_list = [word[0] for word in list]

#4
list = [1,2,3,4,5,6]
new_list = [val for val in list if val % 2 == 0]

#5
list_a = [1,2,3,4]
list_b = [3,4,5,6]
list_int = [val for val in list_a if val in list_b]

#6
list_names = ["Elie", "Tim", "Matt"]
new_list = [val.lower()[::-1] for val in list]

#7
first = "first"
third = "third"
new_string = [val for val in first if val in third]

#8
new_list = [val for val in range(1,101) if val % 12 == 0]

#9
string = "amazing"
consonants = [letter for letter in string if letter not in ["a", "e", "i", "o", "u"]]

#10
new_list = [[i for i in range(0,3)] for num in range(0,3)]

#11
new_list = [[i for i in range(0,10)] for num in range(0,10)]




