# print("Hello World 1", end="\n")
# print(2 * "\n")
# doc string
'''Hello World 2'''  # doc string
# print("Hello World 2")
# block statements for instance
# constant
PI = 3.140

# variables
name = "Fatima B"
# chaneg the value of variable
name = "Fatima O"
# print(name)

# variables are mutable (changeable)
# cannot start with a number
# can use underscore
# can use capital letters (but not recommended only for constants)
# snake_case example: my_variable
# camelCase example: myVariable
# PascalCase example: MyVariable
# variable name should be descriptive
# keywords cannot be used as variable name

# constants
# cannot change after initialization (immutable)
# constants  must be defined with a capital letter

first_name = "Fatima"
firstName = "Fatima"
FirstName = "Fatima"

#  data types (types)
# string example: "Hello World"
# list example: [1, 2, 3]
# character example: 'a'
# tuple example: (1, 2, 3)
# set example: {1, 2, 3}
# dictionary example: {'name': 'Fatima', 'age': '21'}

# LIST
# index starts from 0 for every list
names = ["Fatima O", "Ebunoluwa", "Unknown B", "Name A"]

names[2] = "Fatima BK"
# print the ['Ebunoluwa', 'Fatima BK']
print(names[1:-1])
# print the last 2 elements ["Unknown B", "Name A"]
print(names[-2:])

numbers = [1, 2, 3, 4, 5]
# print [ 2, 3, 4]
print(numbers[1:4])

numbers.append(6)
# print [1, 2, 3, 4, 5, 6]
print(numbers)
# deleting the last element
numbers.pop()
# print [1, 2, 3, 4, 5]
print(numbers)
# adding element at 7 index 2
numbers.insert(3, 7)
# print [1, 2, 3, 7, 4, 5]
print(numbers)
# sort the list from   highest to lowest
numbers.sort(reverse=True)
# print [7, 5, 4, 3, 2, 1]
print(numbers)
# sort the list from   lowest to highest
numbers.sort()
# print [1, 2, 3, 4, 5, 7]
print(numbers)


people = [{'name': 'Ebunoluwa', 'age': '21', "school_attended": "wlv"}, {
    'name': 'Fatima O', 'age': '21'}, {'name': 'Fatima B', 'age': '21'}]
# print(people[2])
#  key and value pairs

# tuples are immutable
names_tuple = ("Ebunoluwat", "Fatima O", "Fatima B")
# convert the tuple to list
names_list = list(names_tuple)
# print the new list ["Ebunoluwat", "Fatima O", "Fatima B"]
print(names_list)
# modify the list index 0
names_list[0] = "Ebunoluwa"

# set the above list back to the tuple
names_tuple = tuple(names_list)
# printing the new tuple ["Ebunoluwa", "Fatima O", "Fatima B"]
print(names_tuple)

# make a new tuple
# make a copy of a tuple and change it as a new tuple

# set
# set is a collection of unique elements

names = ["Ebunoluwa", "Fatima", "Fatima"]
# this should remove the duplicates
names = set(names)
print(names)

# Dictionary
person = {'name': 'Ebunoluwa', 'age': '21', "school_attended": "wlv"}

print(person)
# modifying the dictionary
person['name'] = "Adewale Oluwadamilola"
# adding a new key and value
person['country'] = "Nigeria"

print(person)
# accessing the values
print(person['name'])
#  using the get method to access the value
print(person.get('age'))

# keywords - do not use reserved keywords
# continue
#  pass
# if , else, elif, for, while, def,
# class, return, break, and, or, not, is,
# in, not in, is not, not is, etc

# learn to read your error messages

# data structures
# stack - LIFO
