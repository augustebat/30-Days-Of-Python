#-----------Level 1-----------

#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to learn to drive.')
else:
    print(f'You need {18-age} more years to learn to drive.')


#2 Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 21
your_age = int(input('\nEnter your age: '))

if your_age > my_age:
    if your_age - my_age == 1:
       print(f'You are {your_age - my_age} year older than me.') 
    else:
        print(f'You are {your_age - my_age} years older than me.')
elif your_age < my_age:
    if my_age - your_age == 1:
        print(f'You are {my_age - your_age} year younger than me.')
    else:
        print(f'You are {my_age - your_age} years younger than me.')
else:
    print(f'We both are {my_age} years old.')


#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('\nEnter number one: '))
b = int(input('Enter number two: '))

if a>b:
    print(f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} and {b} are equal.')



#-----------Level 2-----------
#1 Write a code which gives grade to students according to theirs scores:

grade = int(input('\nEnter your grade: '))

if grade >=90 and grade <=100:
    print('Your grade is A.')
elif grade >=80 and grade <=89:
    print('Your grade is B.')
elif grade >=70 and grade <=79:
    print('Your grade is C.')
elif grade >=60 and grade <=69:
    print('Your grade is D.')
elif grade >=0 and grade <=59:
     print('Your grade is F.')
else:
    print('Error.')


#2 Get the month from user input then check if the season 
# is Autumn, Winter, Spring or Summer.
#  If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. 
# March, April or May, the season is Spring 
# June, July or August, the season is Summer

month = str(input('\nEnter a month: '))
if month == 'September' or month == 'October' or month == 'November':
    print('The season is Autumn <3.')
elif month == 'December' or month == 'January' or month == 'February':
    print('The season is Winter <3.')
elif month == 'March' or month == 'April' or month == 'May':
    print('The season is Spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('The season is Summer.')
else:
    print('Error.')

#3 The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('\nEnter a fruit: '))

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print('The modified list: \n', fruits)





#-----------Level 3-----------

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    igudziai = person['skills']
    middle = len(igudziai) //2
    print(f"Middle skill: {igudziai[middle]}")

# Check if the person dictionary has skills key, 
# if so check if the person has 'Python' skill and print out the result
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print(f"if the person has 'Python' skill: {has_python}")


# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

if len(person['skills']) == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

    
# If the person is married and if he lives in Finland, print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

status = person['is_married']
country = person['country']
if status and country == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in Finland. He is married.')