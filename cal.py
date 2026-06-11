# Variable
# Variable: can be refer to as a container holding a value. e.g

# name = 'david'
# age = 25

# l = eval(input('ENETR THE NUMBER'))
# print(l[:5])

# l = ['orange', 'banana', 'pear', 'pizza']
# l[3]= 'apple'
# for i in range(1):
#     print(l, end='')
#     print()

# for loop
# dealing  with for loop

#while loop

# n = 100
# p2 = 1
# while p2 <=n:
#     p2 *= 2
# print(p2)

# # example 2
# num = eval(input('Enter Number:'))
# while num <=3.5:
#     num / 2
# print(num)


#list = ['1. maggi','2. onion','3. curry']
# for i in range(4,0,-1):
#     print(i,'off', end=' ')
# print('blast off')

# for i in range(4):
#     n = int(input('What is the squareroot of :'))
#     print('The squareroot is', n*n)
# print('You are done with this!! ')

# for i in range(5):
#     print('a'*6)#(1+i))

# name = 'delmi'
# for i in range(1,101):
#     print(i, name, end='  ')

# for i in range(1,21):
#     print((i),'---',i*i)

# for i in range(8,90,3):
#     print(i, end=' ')

# for i in range(100,2,-2):
#     print(i, end=' ')

# for i in range(10):
#     print('A', end='')
# for i in range(10):
#     print('B', end='')
# for i in range(4):
#     print('CD', end='')


# Random numbers
# from random import randint
# x = randint(1,20)
# print(x)


# Math functions
# from math import sin, pi, cos
# print(cos)
# print(sin)
# print(pi)

# #Built-in math function
# print(abs(-5.5))
# print(abs(-4.3))
# print(round(345.2,-1))

# import random

# n = random.randint(1,10)
# print(n)


 # temp = eval(input('Enter a temerature in celsius:'))
# print('in Fahrenheit, that is', 9/5*temp+32)

# n1 = eval(input('enter no.:'))
# n2 = eval(input('enter no.:'))
# print('the average is',(n1   n2 /2  ))


# num = eval(input('Enter a number: '))
# print('Your number squared:', numn * num)

# print('what is ur name', sep ='')
# print('my name is melchizedek samson')
# print('5+5 =',5+5, '.')
# print('5+5 =',5+5, '.',sep='')

# for i in range(5):
#     print('Hello')


# for i in range(3): num = eval(input('Enter a number: ')) 
# print ('The square of your number is', num*num) 
# print('The loop is now done.')

# for i in range(3): 
#     print(i+1,'---hello')

# for y in range(100):
#     print(y)

# for y in range(4):
#     print('*'*30)

# for i in range(4):
#     print('*'*(i+2))


# import math

# a = 5

# sin = math.sin(9)
# cos = math.cos(a)
# tan = math.tan(a)

# print(sin)


# import time
# hours = int(input('Enter time in Hours:'))
# minutes = int(input('Enter time in Minutes:'))
# seconds = int(input('Enter time in seconds:'))

# total_seconds = hours*minutes*seconds

# print('\rTimer started...\r')



# while total_seconds > 0:
#     hours = total_seconds // 3600
#     minutes = (total_seconds % 3600) // 60
#     seconds = total_seconds % 60
#     print(f'\rTime:{hours:02d}:{minutes:02d}:{seconds:02d}', end='')

#     time.sleep(1)
#     total_seconds += 1
# print('\rTimes up!')
# try:
#     import  winsound
#     winsound.beep(1000, 1000)
# except:
#     print('Alarm sound not supported on this system.')


# num = eval(input('Enter Number:'))
# print(num)

# print('On the first line','.',end='') 
# print('On the second line','.',sep='')

# rectangle with star
# rows = int(input('Enter rows:'))
# cols = int(input('Enter cols:'))

# for i in range(rows):
#     print('*' * cols)


#Rectangle
# rows = 5
# cols = 10
# for i in range(rows):
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or  j ==  0 or j == cols - 1:
#             print('*', end='')
#         else:
#             print('', end='')
#     print()

# for i in range(3): 
#     num = eval(input('Enter a number: ')) 
#     print ('The square of your number is', num*num) 
# print('The loop is now done.')


# print('A')
# print('B')
# for a in range(3):
#     print('P')
#     print('L')
# print('ED')

# for i in range(3):
#     print(i+5, '-- Hello')

# import time

# x = int(input('Enter the Seconds:'' '))

# while x > 0:
#     sec = x % 60
#     min =(x % 3600) // 60
#     hrs = x // 3600

#     print(f'{hrs:02}:{min:02}:{sec:02}')

#     time.sleep(1)
#     x +=1

# fs = []
# ps = []
# while True:
#     f = input('Enter Food Name or Q to quit:')
#     if f == 'q':
#         break
#     else:
#         p = int(input('Enter The Price:'))
#         fs.append(f)
#         ps.append(p)
#         print()
#         print('....Selected Food......')
#         for f in fs:
#             print(f, end='')
        

#         print('....Total price......')
#         for p in ps:
#             print(p, end='')
#             totla += p

# students = [('John',50),('Marry',80), ('David',44), ('Aisha',75), ('Hebrew',60), ('Delmi',30), ('Blessing',90), ('liveth',20)]


# def get_letter_grade (student_data):
#     name, score = student_data

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
#     return f'{name}: score{score}, grade{grade}'

# graded_result = map(get_letter_grade, student)

# for result in gradeded results:
#     print(result)



# def add(name, age, country, state, lg):
#         print(f"""Your name is {name} and you are {age} years old, your country is, 
#          {country} from {state} {lg}""")


# add('Melchizedek','23','Nigeria','Taraba','Sardauna')

# def sub_add(a,b,c):
#         z = a-b+c
#         print(z)
# sub_add (50,30,1)

# def tadd_add(amount, dc=0.1, tax=0.05):
#     add = amount * (1+dc) * (1+tax)
#     return add
# print(tadd_add(10))  


#POSITIONING ARGUMENT
# def list(name, age,hub,game,favorite):
#     print(f"""My name is {name} and i'm {age} years old, my hubby is {hub}
# and my best game is {game} and my fovuorite food is {favorite}.Thank you all for your 
# time and reading throught'
# {game} is my favorite game
#     See you next on my next video.
#     """)

# list ('Rhuda Dauda','30','Singing and playing of piano','volley ball','Rice')

#SPLIT
# list = 'apple, mango, banann'
# print(list.split(','))


# for i in range(4):
#     print()
# #print('=' * 33)

# def make_cofee():
#     print('start the machine')
#     print('make cofee')
#     print('add milk')
#     print('enjoy it')

# print('wake up')
# make_cofee()
# print('work  for a while')
# make_cofee()


# def multiply_number(v):
#     print(v*5)
# multiply_number(5)

# def cleans_name(name, age):
#     print(name.upper().strip(), age)
# cleans_name('  samson melchizedek    ', '25')


# f = 5
# j = 5
# def add(x):
#     y = f + x * j
#     print(y)
# add(2)

#print('hello world')
# name =  input(' ENETR THE NUMBER: '.strip())
# for i in name:
#     print(name)

# name = input('  Enter Your Name:'.strip())
# role = input('Enter Your Role:  '.strip())
# age = eval(input('  Enter Your Age:'.strip()))

# print(f'Your name is {name.upper()}, your role is {role.upper()} and your age is {age}')
# #print(f'Name: {name.upper()} | Role: {role.upper()} | Age: {age} Year')




# str = '968-maria, (d@t@ Engineer );; 27y    '.strip().capitalize()

# print(str.replace('968-maria,', 'name: maria |').replace('(','').replace(');;','').replace('d@t@','role: data')
# .replace(' 27y','| age: 27 years'))


# lists = [' apple','yam','banana','mango','plantain']
# for list in lists:


#     print(list.strip())
# for i in range(5, 0, -1):
#     print(i)

#print('odd' if 40 % 2 else 'even')
#age = 5
# while age < 0: 
    
#     age = int(input('ENTER AGE: '))

#username = 'melchizedek'

#print(username[1:])
#print('positive' if 5 > 0 else 'negative'

# n1 = 8
# n2 = 9
# n3 = n1 > n2
# print(f"n1 = {n1}, n2 = {n2}, n3 = {n3}")


# a = 5
# b = 11

# # Don't change below this line
# c = 0
# if a >= b and not b < 10:
#     c = 5

# c += 1
# print(f"c = {c}")


# user = {"name": "Alice", "age": 25}
# user["name"] = 'g'
# print(user)
# user = {"name": "Alice", "age": 25}
# user.update({"age": 27, "city": "New York"})
# print(user)



# class fruit:
#     def __init__(self, name, color, category):
#         self.name = name
#         self.color = color
#         self.category = category

# f = fruit('orange','red','fruit')

# print(f'{f.name} {f.color} {f.category}')

# class book:
#     def __init__(self, b1, b2, b3):
#         self.b1 = b1
#         self.b2 = b2
#         self.b3 = b3

# b0 = book('math book 1','english book 2','physics book 3')

# print(f'{b0.b1} {b0.b2} {b0.b3}')

# class house:
#     house = 'Flat'
#     def __init__(self, room1, room2, room3):
#         self.room1 = room1
#         self.room2 = room2
#         self.room3 = room3
#         print()
# bo = house('Master bedroom','Normal bedroom','Visitor bedroom')

# # print(bo.house)
# # print(bo.room3)

# class unit:
#     def __init__(self, h, t, u):
#         self.h = h
#         self.t = t
#         self.u = u

# num = unit(100, 10, 0)
# print(num.h)


# WHILE CONDITION LOOP
# name = ""
# while name != 'delmi':
#     name = input('Enter the name: ') 
# print('Thank You')

# answer = ""
# while answer !='delmi':
#     answer = input('Enter the name: ')
# print('Thank You')

# count = 0
# while count < 3:
#     ansa = input('do you agree with me:')

#     if ansa == 'yes':
#         print('glad u did')
#         count = count + 2


# WHILE TRUE LOOP
# while True:
#     answer = input('Do you love me? Yes or No: ')
#     if answer == "yes":
#         print('Correct')
#         break
#     else:
#         print('Try again')
# print('Good Job')

# class person:
#     def __init__(self, name, age, local, state, country):
#         self.name = name
#         self.age = age
#         self.local = local 
#         self.state = state
#         self.country = country

# human = person('delmi', 23, 'Sardauna Local Government', 'Taraba', 'Nigeria')

# print(f"""My name is {human.name}. And i\'m {human.age} years old.
# I\'m from  {human.local}, {human.state}, of {human.country}""")




print()
print('Welcome to sit technology hub, we are glad to have you here!!\n')

print("""We are a technology hub that is focused on training and empowering 
young people with digital skills to thrive in the digital economy.
Our mission is to bridge the digital divide and create opportunities for, 
young people to succeed in the digital world.\n""")

print('How may we help you today?')

print('1. Register')
print('2. Login')
print('3. Exit\n')


print('......Enter your details below to get started....')
class person:
    def __init__(self, name, age, dob, course, address):
        self.name = name
        self.age = age
        self.dob = dob
        self.address = address
        self.course = course

name = input('Enter your full name: ')
age = int(input('Enter your age: '))
dob = input('Enter your date of birth: ')
address = input('Enter your address: ')
course = input('Enter your course: ')
human = person(name=name, age=age, dob=dob, address=address, course=course)

#print(human.name, human.age, human.local, human.state, human.country)

print()
print(f"""Your name is {human.name}. And you are {human.age} years old.
Your date of birth is {human.dob}. You came from  {human.address},
and the course you will pursue is {human.course}""")
print()
is_u = input('Confirm the infomation you entered above is legit? True or False: ')
is_u = is_u.lower()
while is_u == 'true':
    print()
    print('..........Thank you for confirming your Details...........')
    print()
    print('........WELCOOME TO SIT TECHNOLOGY HUB..........,')
    print('We are excited to have you on board and we look forward to seeing you thrive in the digital world!!')
    break
else:     
    print('Please re-enter your info')


