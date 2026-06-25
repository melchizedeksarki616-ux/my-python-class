# class Car:
#     def __init__(self, color, model, year):
#         self.color = color
#         self.model = model
#         self.year = year

# my_car = Car("red", "Toyota", 2020)

# print(my_car.color)
# print(my_car.model)

# class Car:
#     def __init__(self, color, model, year):
#         self.color = color
#         self.model = model
#         self.year = year

#     def start(self):
#         print(f'{self.model} {self.year}  is starting')
#     def describe(self):
#         print(f'my car is a {self.color} color {self.model} {self.year}')

# my_car = Car("red", "Toyota", 2020)
# my_car2 = Car('blue', 'honda', 2024)


# my_car2.start()
# my_car.start()
# my_car.describe()

# class Student:
#     def __init__(self, name, age, gpa):
#         self.name= name
#         self.age = age 
#         self.gpa = gpa

#     def describe(self):
#         print(f" hi my name is {self.name} and i am {self.age} and my gpa is {self.gpa}")


# student1 = Student('emmanuel', 55, 5.0)
# student2 = Student('john', 66, 4.7)


# student1.describe()
# student2.describe()

class Bank:
    bank_name = 'Gtbank'
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


user1 = Bank('Emmanuel', 70000)
user2 = Bank('john', 5000)

print(user1.bank_name)
print(user2.bank_name)
print(user1.name)
print(user2.name)