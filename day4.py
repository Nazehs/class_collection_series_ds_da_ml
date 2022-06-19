# using the filter function to filter out the odd numbers


from functools import reduce


numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10]


# def filterNumbers(number):
#     if number % 2 == 0:
#         return True


# filtered = list(filter(filterNumbers, numbers))

# print(filtered)


# filtered_lambda = list(filter(lambda x: x % 2 == 0, numbers))

# print(filtered_lambda)


result = map(lambda num: num * 2, range(1, 11))

# print(list(result))

filtered = filter(lambda num: num == 2, numbers)

# print(list(filtered))

# reduce function

print(reduce(lambda x, y: x + y, numbers), sum(numbers))

# give numbers then i will add them up and return the result

# switch statement

# syntax of switch statement
#  switch (expression):
#  block of code

operator = "+"


# match operator:
#     case "+":
#         print("Addition")
# switch (operator):
#     case "+":
#         print("Addition")


# OOP - Object Oriented Programming

# class name:
#  block of code


# class is a blueprint for creating objects
# class is a template for creating objects

# constructor - is a function that is called when you create an object

class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def displayBio(self):
        return("Hello, " + self.name + " \nage: " +
               self.age + "\ngender: " + self.gender)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def greetPerson(self):
        return 'Good Morning, ' + self.name


class Manager(Person):
    def __init__(self, name, age, gender, email):
        self.email = email
        super().__init__(name, age, gender)

    def getEmail(self):
        return self.email


class People(Manager):
    def __init__(self, name, age, gender, email, location):
        self.location = location
        super().__init__(name, age, gender, email)

    def getLocation(self):
        return self.location


if __name__ == '__main__':
    people = People("Nazeh Abel", "35", "Male",
                    "email@email.com", "Birmingham")

    print(people.getEmail())
    person = Person("Nazeh Abel", "35", "Male")
    bio = person.displayBio()
    manager = Manager("Nazeh Abel", "35", "Male", "email@email.com")

    print(manager.getEmail())

    print(person.getName())
