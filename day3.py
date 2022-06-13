# iterators
# for loop
# while loop

#  syntax of for loop
#  for <variable> in <iterable>:
#        block of code

names = ['John', 'Bob', 'Mary', 'Jane', 'Jack', 'Joe']

# print(names[0])

# print(names[1])

# print(names[2])

# print(names[3])

# print(names[4])

# for name in names:
#     print(' Hello ' + name)

# while loop

# syntax of while loop

# for index, name in enumerate(names):
#     print(index, name)

# while condition:
#     block of code
# count = 0
# while count < len(names):
#     print('Hello ' + names[count])
#     count += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#         break


# for i in numbers:
#     if i % 2 == 1:
#         print(' from 2 ', i)
#         continue

# strings and manipulation

# name = "nazeh|abel|something anothing"

# name2 = "NAZEH DUMMMYY"

# print(name.capitalize())

# print(name.upper())

# print(name2.lower())

# print(name.title())

# print(name.split())

# print(name.split(' '))

# print(name2[:-3])

# print(name2[-3:])

# print(name2.find('A'))

# print(''.join(reversed(name2)))

# name2 = name2.replace('DUMMMYY', 'Z')

# print(name2)

#  functions


# syntax of function

# def function_name():
#  block of code
# without parameters
# def sayHello():
#     print('Hello There!')
#     print('Hello again!')
# sayHello()
# with parameters
# def sayHello(name):
#     print('Hello ' + name)
#     print('Hello again ' + name)

# sayHello("Nazeh")

# with optional parameters
# def sayHello(name=""):
#     print('Hello ' + name)
#     print('Hello again ' + name)


# sayHello()


# def sum(num1, num2):
#     total = num1 + num2
#     # print(result)
#     return total


# result = sum(6, 2)

# print(result)

# for name in names:
#     print('Hello ' + name)

# for num in range(3, 11, 2):
#     print(num)

# for index, name in enumerate(names):
#     print(index, name)


print(int(3.0))
print(float(3))

print(round(3.5))

print(abs(4.81344))

print(sum([6, 2, 3, 4, 5, 10, 11]))


# build a calculator
# take  a list a numbers and find duplicates from the list
# take a list of numbers and find the sum of all the numbers
# take a list of numbers and find the average of all the numbers
# take a list of numbers and find the maximum number
