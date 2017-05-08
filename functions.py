# Katie Krieger
# 5/7/17

# https://www.rithmschool.com/courses/python-fundamentals-part-1/python-functions-exercises

# Part 1

#1
def difference(a,b):
	return a-b

def product(a,b):
	return a*b

def print_day(num):
	if num < 1 or num > 7:
		return None
	dict = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
	return dict[num]

def last_element(list):
	if len(list) == 0:
		return None
	return list[-1]

def number_compare(num1, num2):
	if num1 > num2:
		return "First is greater"
	elif num2 > num1:
		return "Second is greater"
	return "Number are equal"

def single_letter_count(word, letter):
	return word.count(letter.upper()) + word.count(letter.lower())

def multiple_letter_count(str):
	return {letters: str.count(letters.upper()) + str.count(letters.lower()) for letters in str}
	
def list_manipulatin(list, cmd, loc, value):
	if cmd == "remove" and loc == "end":
		return list.pop()
	elif cmd == "remove" and loc == "beginning":
		return list.pop(0)
	elif cmd == "add" and loc == "beginning":
		list.insert(0, val)
		return list
	elif cmd == "add" and loc == "end":
		list.append(val)
		return list

def is_palindrome(str):
	str = str.replace(" ","").lower()
	return str == str[::-1]

def frequency(list, search_term):
	return list.count(searchTerm)
	#return len([term for term in list if term == search_term])

def flip_case(str, letter):
	return "".join(
		[char.swapcase() if char.lower() == letter.lower() 
		else char 
		for char in string])
	# for char in str:
	# 	if char == letter and char.islower():
	# 		char.upper()
	# 	elif char == letter and char.isupper():
	# 		char.lower()
	# 	else:
	# 		char
	# return str

def multiply_even_numbers(list):
	even_list = [num for num in list if num % 2 == 0]
	result = 1
	for vals in even_list:
		result *= vals
	return result

def mode(list):
	count = {vals: list.count(vals) for vals in list}
	max_value = max(count.values())
	correct_index = list(count.values()).index(max_value)
	return list(count.keys())[correct_index]
	# NOT WORKING FOR ME ??? 

def capitalize(str):
	return str[0].upper() + str[1:]

def compact(list):
	return [item for item in list if item]

def partition(list, fn):
	return [[val for val in list if fn(val)], [val for val in list if not fn(val)]]
	# list_true = []
	# list_false = []
	# for el in list:
	# 	if fn(el) == True:
	# 		list_true.append(el)
	# 	else:
	# 		list_false.append(el)
	# return [list_true, list_false]

def intersection(list_1, list_2):
	return [item for item in list_1 if item in list_2]

def once(fn):
	# returns a new fn that can only be invoked once
	# if invoked more than once, should return None
	def inner(*args):
		inner.count += 1
		if inner.count == 1:
			return fn(*args)
		else:
			inner.count += 1
			return None
	inner.count = 0
	return inner


