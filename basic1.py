
#PYTHON BASIC

#print() funtion
# print("Hello World, i'm learning python")

# input() function
# input = input('Enter your name: ')

# input
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# print(f' happy birthday {name} your {age} years old today')


# Special characters.
#  \"     double quote  
#  \'     single quote  
#  \\     back slash  
#  \n     new line  
#  \t     tab
#  \b     4 backspace


#Variable
#name = 'Delmi'  # string
#age = 25        # integer
# gpa = 3.35      # float
# is_student = True    # boolean
# not_student = False # boolean

# print(f'my name is {name}  and i\'m {age} years old')

#Conversion
# age = bool(age)
# name = bool(name)
# gpa = bool(gpa)
# isstudent = int(isstudent)


#Functions
#input()
#print('name')           # 
# print(type(name))     #value type() checking
#print(len(name))       len of value


#Method
age = 50
age.bit_length()        #value.method
name = 'delmi'
name.upper()            value.method







# Values Types (hard coded and dynamic values)
# country = 'Nigeria'                  #hard coded
# country = input('Enter country:')    # dynamic


#Data types in Python
    #Data Types Categories
# 1. no value
# 2. premitive(single values)
#     int=50, float=3.45, str='hello', bool=True
# 3. multiple values.   like
#     list["apple", "mango"],
#     tuple("apple", "mango"),
#     set{"apple", "mango"},
#     dictionary{"name":"Delmi", "country":"Nigeria"} 







# Examples

# #area of a rectangle
# length = float(input('Enter the length: '))
# breath = float(input('Enter the breath: '))

# area  = length * breath 

# print(f'the area of a rectaangle is {area}')



# # Volume of a rectangle
# length = float(input('enter the length:  '))
# width = float(input('enter the width: '))
# heigh = float(input('enter the heigh:  '))

# volume = length * width * heigh

# print(f'The volume of a rectangle is {volume}')


# # circumference of a circle, find using diameter
# pi = float(input('enter the pi:'))
# diameter= float(input('enter the d:'))
# circumference = pi * diameter
# print(f'The circumference of a is: {circumference}')


# circumference of a circle, find using radius
# radius= float(input('Enter the Radius:'))

# circumference = 2 * math.pi * radius

# print(f'The circumference of a is: {circumference}')

# item = input('enter the Item: ')
# quantity = int(input('Enter the qantity: '))
# price = float(input('enter the ammount'))

# total = quantity * price

# print(f'your item {item} tottal is {total}')

# x = 5
# #or 
# print(x<2 or x>4)
# # and
# print(x>2 and x>4)
# # not
# print(not(x>10))



# import math
# a = 10.1
# b = 6
# c = 3

# print(a + b)
# print(a -b)
# print(a * b)
# print(a / b)
# print( a ** b)
# print( a % b)
# print(round(a))
# print(math.floor(a))
# print(math.ceil(a))
# print(pow(a,b))
# print(min(a,b,c))
# print(max(a,b,c))
# print(math.sqrt(a))

# constant
# print(math.e)
# print(math.pi)
# print(math.cos)
# print(math.sin)
# print(math.tan)

# a = 2
# if a % 2  :
#     print('odd')
# else:
#     print('even')

# age = int(input('enter your age'))

# if age >=100:
#     print('youre too old to vote')
# elif age >=18:
#     print('youre eligable to vote')
# elif age<=0:
#     print('this is not a valid age')
# else:
#     print('youre under age')


# response = input('are you a student y/n : ')

# if response == 'y':
#     print('welcome to school')
# elif response == 'n':
#     print('youre not a student here')
# else:
#     print('enter a valid response')


# ansa = input('Are u a christian?')

# if ansa == 'yes':
#     print('save path')
# elif ansa == 'no':
#     print('u need to be one')
# else:
#     print('u are not serious')

# ASSIGNMENT
# WRITE A PYTHON CODE TO OUTPUT STUDENT'S GRADE WHEN ENTERED.
    #Test is over 20 each and Exam is over 60.
# print('Enter Your Maths Score Bellow:')
# test1 =float(input('Enter first C.A Test Score:'))#E.g test score= 15
# test2 = float(input('Enter Second C.A Test Score:'))#E.g test score= 18
# exam = float(input('Enter Examination Score:')) # score= 50

# total = test1 + test2 + exam
# average = total/3

# if total >=70:
#     grade = 'A'
# elif total >=60:
#     grade = 'B'
# elif total >=50:
#     grade ='C'
# elif total >=44:
#     grade = 'D'
# elif total >=40:
#     grade = 'E'
# else:
#     grade = 'F'

# print(total)
# print(average)
# print(f'With the above total and average, your Grade is:{grade}')





# BALANCE = 0.00
# deposit = float(input('Enter the ammount you want to deposit: '))

# current_balance = balance + deposit

# print(f'Your current balance is ${current_balance}')

# withdrawal = float(input('Enter the ammount you wan to withdraw'))

# present_balance = current_balance - withdrawal

# if current_balance < withdrawal:
#     print(f'insufficient funds and your balance is {current_balance} ')
# else:
#     print(f' sucessfull you have withdrawn {withdrawal} and your current balance is {present_balance}')

# ammount = 100000

# water = float(input('Enter the water bill ammount'))
# light = float(input('Enter the light bill ammount'))
# education = float(input('Enter the education bill ammount'))
# outing = float(input('Enter the outing bill ammount'))
# food = float(input('Enter the food bill ammount'))

# total_spent =water + light + education + outing + food
# print(f' you spent a toatal of ${total_spent} this month')

# total_savings =  ammount - total_spent

# if total_spent >ammount:
#     print(f'  youre in debt of ${total_savings}')
# else:
#     print(f'you saved ${total_savings}')

# import math
# num1 = float(input('Enter the number:'))
# operator = input('Enter the operator:')
# num2 = float(input('Enter the number:'))

# if operator == '+':
#     print('Result: ', num1 + num2)
# elif operator == '-':
#     print('Result: ', num1 - num2)
# elif operator == '/':
#     print('Result:',num1 / num2) 
# elif operator == '*':
#     print('Result:',num1 * num2)
# elif operator == 'sin':
#     print(num2, math.sin(num1))

# import time

# seconds =  int(input('Enter seconds:'))


# print('\rTime Started......\r')

# while seconds > 0:

#     hours = seconds //  3600
#     minutes  = (seconds % 3600)  // 60
#     seconds = seconds % 60

#     print(f'\r{hours:02}:{minutes:02}:{seconds:02}', end='')

#     time.sleep(1)
#     seconds +=1
# print('\r Time out...!\r')

# ASSIGNMENT

# students = ['John','Marry','David','Aisha','Hebrew', 'Delmi', 'Blessing', 'liveth']
# scores = [50, 80, 44, 75, 60, 30, 90, 20]

# def get_grade (score):
#     if score >= 80:
#         return 'A'
#     if score >= 70:
#         return 'B'
#     if score >= 60:
#         return 'C'
#     if score >= 50:
#         return 'D'
#     if score >= 40:
#         return 'E'
#     else:
#         return 'F'

# grades = list(map(get_grade, scores))
# print(grades)
# for i in range(len(students)):
#     print(students[i], scores[i], grades[i], sep='   ')

# for student in students:
#     print(student)


# questions = (
#     'This are group of people?',
#     'Is he a student of this school?',
#     'Are you from cameroon?',
#     'do you teach?')

# options = (('True',or'False'),('True',or'False'),('True',or'False'),('True',or'False'))

# answers = ('T','F','F','T',)
# guesses = []
# score = 0
# question_numbers = 0

# for question in questions:
#     print('::::::::::::::::::::::::::::::::::')
#     print(question)

#     for option in options[question_numbers]:
#         print(option)

#     guess = input('Enter Answer T or F:')
#     guesses.append(guess)

# /
#     if guess.upper() == answers[question_numbers]:
#         score +=1
#         print('correct')
#     else:
#         print('not correct')
#         print(f'The correct answer is:{answers[question_numbers]}')
#     question_numbers +=1

# print('...........Result...........')
# print('............................')
# for guess in guesses:
#     print(guess, end='')
# print()
# for answer in answers:
#     print(answer, end='')
# print()

# score = int(score/ len(questions) *100)
# print(f'{score}%')






#A SIMPLE INVENTORY MANAGEMENT SYSTEM

# inventory = {}

# def add_item():
#     name = input('Enter item name: ').lower()
#     quantity = int(input('Enter quantity: '))
#     price = float(input('Enter the price: '))


#     inventory [name] = {'quantity': quantity, 'price': price}
#     print(f'{name} added successful.\n')

# def view_inventory():
#     if not inventory:
#         print('Inventory is empty.\n')
#         return
#     print('\n----Inventory---')
#     for name, details in inventory.items():
#         print(f'item: {name}')
#         print(f'  Quantity:{details['quantity']}')
#         print(f'price: N {details["price"]}')
#         print()
# def update_item():
#     name = input('Enter items name to update:').lower()
#     if name in inventory:
#         quantity = int(input('Enter new quantity:'))
#         price = float(input('Enter the price:'))
#         inventory [name] ['quantity'] = quantity
#         inventory [name] ['price'] = price
#         print(f'{name} updated successfully.\n')
#     else:
#         print('Item not found.\n')
# def delete_item():
#     name = input('Enter items name to delete:').lower()
#     if name in inventory:
#         del inventory [name]
#         print(f'{name} updated successfully.\n')

#     else:
#         print('Item not found.\n')

# def menu():
#     while True:
#         print('=====Inventory Menu=======')
#         print('1. add item')
#         print('2. view inventory')
#         print('3. update item')
#         print('4. delete item')
#         print('5. exit')

#         choice = input('choose an options: ')
#         if choice =='1':
#             add_item()
#         if choice =='2':
#             view_inventory()
#         if choice =='3':
#             update_item()
#         if choice =='4':
#             delete_item()
#         if choice =='5':
#             print('exiting progam......')
#             break
#         elif not choice:
#             print('invalid choice. try again.')

# menu()

