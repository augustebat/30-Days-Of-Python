#-----------Level 1-----------
#1 Iterate 0 to 10 using for loop, do the same using while loop.
print('\nFOR ciklas')
for number in range(11):
    print(number)

print('\nWHILE ciklas')
number = 0
while number<=10:
    print(number)
    number+=1

#2 Iterate 10 to 0 using for loop, do the same using while loop.
print('\nFOR ciklas einant atgal')
for number in range(10, -1, -1):
    print(number)

print('\nWHILE ciklas einant atgal')
number = 10
while number>=0:
    print(number)
    number-=1


#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
"""
  #
  ##
  ###
  ####
  #####
  ######
  #######
"""
simbolis = ''
i=0
for i in range(8):
    print(simbolis)
    simbolis+='#'


#4 Use nested loops to create the following:
"""
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
"""
print()
i=0
j=0
for i in range (8):
    eilute = ''
    for j in range(9):
        eilute+='# '
    print(eilute)

#5 Print the following pattern:
"""
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
"""
print()
i = 0
for i in range(11):
    rezultatas = i * i
    print(f"{i} x {i} = {rezultatas}")


#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print()
items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in items:
    print(item)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
i=0
print('\nEven numbers:')
for i in range(101):
    if i % 2 == 0:
        print(i)

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
i=0
print('\nOdd numbers:')
for i in range(101):
    if i % 2 != 0:
        print(i)




#-----------Level 2-----------

#1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
i = 0
for i in range(101):
    sum+=i

print(f'The sum of all numbers is {sum}.')

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

evens_sum = 0
odds_sum = 0
i=0
for i in range(101):
    if i % 2 == 0:
        evens_sum+=i
    else:
        odds_sum+=i

print(f'The sum of all evens is {evens_sum}. And the sum of all odds is {odds_sum}.')


#-----------Level 3-----------

#2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_list = []

for fruit in fruits:
    reversed_list.insert(0, fruit)
print(fruits)
print(reversed_list)


