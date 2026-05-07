# print("Please enter a number: ")
# number = input()
# print("Value =", number)


# import math
# a = 3
# b = 20
# c = 5
# print(math.floor(a))
# print(math.ceil(a))
# print(round(a))
# print(math.sqrt(b))
# print(max(a,b,c))
# print(min(a,b,c))
# print(pow(a,b))

# total = b*b*b
# print(total)
# print(a+c)
# print(a+b-c)
# print(round(a,b))

# print(math.e)
# print(math.cos)
# print(math.sin)
# print(math.pi)


# # circumference of a circle

# radius = float(input('Enter Radius:'))
# print
# c = 2 * math.pi * radius
# print(f'Circumference is: {c}')


# grading
# print('MY NAME IS DAVE, I AM IN S S 3')
# print('i will enter my scores on computer below for u to know my Grade.')

# t1 = float(input('1st test score:'" "))
# t2 = float(input('2nd test score'" "))
# exam = float(input('exam sscore:'" "))


# total = t1+t2+exam
# average = total/3

# if total >= 70:
#     grade = 'A'
# elif total >= 60:
#     grade = 'B'
# elif total >= 50:
#     grade = 'C'
# elif total >= 45:
#     grade = 'D'
# elif total >= 40:
#     grade = 'E'
# else:
#     grade = 'F'

# print(total)
# print(average)
# print(f'YOUR GRADE IS:{grade}')

# n1 = int(input('Enter No:'))
# op = input('Enter operator:')
# n2 = int(input('Enter No:'))

# if op == '+':
#     print(n1+n2)
# elif op == '-':
#     print(n1 - n2)
# elif op == '/':
#     print(n1 / n2)
# elif op == '*':
#     print(n1 * n2)

# print(True + True)
# print(True + False)
# print(False + False)

# #Comparison
# #==
# print(5==5)
# print(5==3)
# print(5!=4)
# print(5>8)
# print(5<3)
# print(5<=5)



# for y in range(1):
#     print('*'*30)
# for y in range(1):
#     print('*'*2)



# import time
# from datetime import datetime

# while True:
#     current_time = datetime.now().'Strftime'('%H:%M:%S')
#         print(f'clock: {current_time}', end='\r', flush=True)
#         time.sleep(1)
# print('\nClock stopped.')


# import time
# total_seconds = int(input('Enter time in seconds:'))
# seconds = 0

# while seconds <= total_seconds:
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 3600
#     seconds = seconds % 60
#     print(f'\rTime:{hours:02d}:{minutes:02d}:{seconds:02d}', end='')
#     time.sleep(1)
#     seconds += 1
# print('\rTime completed!')


# foods = []
# prices = []
# total = 0

# while True:
#     food = input('Enter food name or q to quit:')
#     if food.lower() =='q':
#         break
#     else:
#         price = int(input('Enter the price:'))
#         foods.append(food)
#         prices.append(price)

#     print('-----ur cart--------')
#     for food in foods:
#         print(food, end=' ')
#         print()
#     print('--------ur total-------')
#     for price in prices:
#         print(price, end=' ')
#         total += price
#         print()
#     print(f'ur total is :{total}')



# for i in range(10):
#     count = 10-i
#     print(''*count//2)
#     print(i,'*'*(i+1))

# ATM MACHINE
# balance = 0.00
# print(f'Your balance is:{balance}')
# depo = float(input('Enter the amount u want to deposit:'))
# balance = depo
# print(f'Ur balance is:{balance}' )
# withd = float(input('Enter the amount u want to withdraw:'))
# if balance < withd:
#     print('insufficient fund')
# else:

#     print(f'Your balance is:{balance-withd}')

# letters = ('A','B','C','D','E','F','G','H')
# options  = (('T','F'),('T','F'),('T','F'),('T','F'),('T','F'),('T','F'),('T','F'),('T','F'))

# answer = (1,2,3,4,5,6,7,8)
# guesses = []
# score = 0
# question_no = 0

# for i in letters:
#     print(i)
#     num = eval(input('Enter any guessing ansswer number: '))
#     guesses.append('guess')

#     for option in options[question_no]:
#         print(option, end='')

#     if guesses == answer[question_no]:
#         print('u are right')
#     else:
#         print('u fall this q.')


# questions = (
#     'This are group of people?',
#     'Is he a student of this school?',
#     'Are you from cameroon?',
#     'do you teach?')

# options = (('a. True', 'b. False'),('a. True', 'b. False'),('a. True', 'b. False'),('a. True', 'b. False'))

# answers = ('a','b','b','a',)
# guesses = []
# score = 0
# question_numbers = 0

# for question in questions:
#     print('::::::::::::::::::::::::::::::::::')
#     print(question)

#     for option in options[question_numbers]:


#         guess = input('Enter Answer a or b:')
#         guesses.append(guess)

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


# dict = {'Delmi Sarki' : 'You are 22 Years Old','Dave Linus' : 'You are 27 Years Old',
# 'Stella Samson' : 'You are 19 Years Old','Joy Genesis' : 'You are 17 Years Old',
# 'Rita Febzir' : 'You are 32 Years Old','linus Peter' : '4You are 44 Years Old'}
# for key, value in dict.items():
#     print(f'{key}:{value}')


import random
options = ('1','2','3')

player  = None
computer = random.choice(options)

while player not in options:
    print('::::::COMPUTER GAME::::::')
    player = input('Enter An Option Guessing Number : ')
    
print(f'player choice : {player}')
print(f'compter choices : {computer}')
if player == 'computer':
    print('tie')
elif player == '1' and computer == '2':
    print('player wins')
elif player == '2' and computer == '3':
    print('player wins')
elif player == '3' and computer == '1':
    print('player wins')
else:
    print('computer wins')
