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