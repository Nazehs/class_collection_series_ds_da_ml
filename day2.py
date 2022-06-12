#  continuation

# get the length of the list

fruits = ["apple", "banana", "cherry"]

# print(len(fruits))

# delete the last element
del fruits[2]

# print(fruits)
# print(len(fruits))

person = {'name': 'Ebunoluwa', 'age': '21', "school_attended": "wlv"}
# deleting the key value pair of age
del person['age']
#  print {'name': 'Ebunoluwa', 'school_attended': 'wlv'}
# print(person)

person_copy = person.copy()

person_copy['age'] = '21'
# expecting {'name': 'Ebunoluwa', 'school_attended': 'wlv'}
# print(person_copy)

# expecting a copy of the original list e.g ['apple', 'banana']
# print(fruits.copy())

#  getting the keys of the dictionary
# expecting a list of keys ['name', 'school_attended']
# print(list(person.keys()))

#  getting the values of the dictionary

# expecting a list of values ['Ebunoluwa', 'wlv']
# print(list(person.values()))

# items of the dictionary
# expecting a list of tuples of key value pairs [('name', 'Ebunoluwa'), ('school_attended', 'wlv')]
# print(list(person.items()))

# update a dictionary
new_features = {'height': '6ft', 'weight': '160lbs'}
person.update(new_features)

# expecting {'name': 'Ebunoluwa', 'school_attended': 'wlv', 'height': '6ft', 'weight': '160lbs'}
# print(person)


# Operators
# arithmetic_operators = {'+': 'addition', '-': 'subtraction', '*': 'multiplication', '/': 'division', '%': 'modulus'}
# comparison_operators = {'==': 'equal to', '!=': 'not equal to', '<': 'less than', '>': 'greater than', '<=': 'less than or equal to', '>=': 'greater than or equal to'}
#  bitwise_operators = {'&': 'bitwise AND', '|': 'bitwise OR', '^': 'bitwise XOR', '~': 'bitwise NOT'}
#  assignment_operators = {'=': 'assignment', '+=': 'add and assign', '-=': 'subtract and assign', '*=': 'multiply and assign', '/=': 'divide and assign'}

# concatenation_operators = {'+': 'concatenation'}

# print("Hello" + " " + "World")
# print(3 + 2)

percent30 = 30
percent60 = 60

result = percent60 // percent30

# print(result, end="")
#  expecting 1
# print(3 - 2)

# expecting 6
# print(3 * 2)

# expecting 1.5
# print(81 / 3)

# expecting 1
# print(3 % 2)

# comparison_operators

num1 = 3
num2 = 4
# EXPECTING FALSE
# print(num1 == num2)
# EXPECTING FALSE
# print(num1 > num2)

# EXPECT FALSE
# print(num1 >= num2)

# EXPECT TRUE
# print(num1 < num2)
# EXPECTING TRUE
# print(num1 <= num2)
# expecting True
# print(num1 != num2)

# BITWISE OPERATORS

# bitwise AND
# print(num1 & num2)

# print(num1 or num2)

# assignment operators

num1 = 3
# expecting 3
# print(num1)
num1 += 1
# expecting 4
# print(num1)

num1 -= 2
# expecting 2
print(num1)

num1 *= 2
# expecting 4
# print(num1)

num1 //= 2
# expecting 2
# print(num1)

# BODMAS

# float and int
# float are decimals e.g. 3.14
# int are whole numbers e.g. 3

# print(3.14 + 2)

# print(int(9/3))

# print(float(3))

# conditional statements

# if statement
# syntax:
# if condition:
#  block of code

age = int(input("How old are you? "))

# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You are not old enough to vote")


if age >= 18 and age <= 45:
    print("You are old enough to vote!")
elif age >= 46 and age < 65:
    print("You are old enough to vote but you not old enough to retire")
elif age >= 65:
    print("You can not vote anymore you should retire!")
else:
    print("You are not old enough to vote")

# ask a user to enter a number
#  check if the number is even or odd

# as user enter  2 numbers
# check the largest number

# as a user enter 2 numbers
# give them the option to add, subtract, multiply or divide them

