# print('...................................................')
# print('             "THIS IS MY HEADING"                    ')
# print('...................................................')

# print("""THE FOLLOWING ARE THE MOST COMMON FRUIT IN GEMBU\n\t1. APPLE\n\t2. MANGO\n\t3. WATER MELLON""")
# print('...................................................')
# print('...................................................')
# for i in range(1):
#     print('"Enter Four Differnt Common Fruit In Your Locality"')
#     print('...................................................')
#     f1 = input('Enter Fruit 1 :')
#     f2 = input('Enter Fruit 2 :')
#     f3 = input('Enter Fruit 3 :')
#     f4 = input('Enter Fruit 4 :')
#     print('....BELOW ARE THE FRIUT LISTED ABOVE.....')
#     print(F'\t{f1},{f2},{f3},{f4}')


# # INTRODUCTION TO PYTHON
# #alpha = 'abcdef'
# names = 'dauda,peter,hanatu'
# print(names.replace('peter','dave'))


# isstudent = True
# num = 55685
# text = 'aswd.erf'
# print(text.replace('.','//'))
# print(type(text))
# print(type(age))
# print(type(isstudent))
# print(text.replace('f','00000'))
# print(len(text))
# print(num.bit_length())


# questions = (
#     'This are group of people?',
#     'Is he a student of this school?',
#     'Are you from cameroon?',
#     'do you teach?')

# options = (('True','False'),('True','False'),('True','False'),('True','False'))

# answers = ('T','F','F','T',)
# gueses = []
# score = 0
# question_numbers = 0

# for i in questions:
#     print(i)

#     for i in options[question_numbers]:
#         print(i)

#     gues = input('choose ansa from above and enter it here:')
#     gueses.append(gues)

#     if gues.lower() == answers[question_numbers]:
#         score +=1
#         print('Correct')
#         print('=====================================================')
#     else:
#         print('Not Correct')
#         print(f'The correct answer is:{answers[question_numbers]}')
    
#         question_numbers +=1
# print('=====================================================')
# print('========================RESULT=======================')
# print('=====================================================')

# for i in answers:
#     print(i, end='')

# print()

# print(score/len(questions)*100)





# print('i made a chnages')

# print('i made a new changes')

# print(This is another changes)


# email = 2.5
# print(email == None and email != '')
# print(type(email))

pw = '1234567890'
print(len(pw))
if len(pw) <10:
    print('Your Password is Too short')
else:
    print('It\'s Greater Than Ten')