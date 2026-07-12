#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
sakinys = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(sakinys)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
sakinys2 = 'Coding' + ' ' + 'For' + ' ' + 'All' 
print(sakinys2)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string
print(company[0:6])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))
print(company.index('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
company_new = 'Python for Everyone'
print(company_new)
print(company_new.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
sakinys3 = 'Coding For All'
print(sakinys3.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
imones = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(imones.split(','))

#15 What is the character at index 0 in the string Coding For All.
print(sakinys3[0])

#16 What is the last index of the string Coding For All.
print(len(sakinys3) - 1)

#17 What character is at index 10 in "Coding For All" string.
print(sakinys3[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
tekstas = 'Python For Everyone'
zodziai = tekstas.split()  
akronimas = zodziai[0][0] + zodziai[1][0] + zodziai[2][0]
print(akronimas)  

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
tekstas2 = 'Coding For All'
zodziai2 = tekstas2.split()
akronimas2 = zodziai2[0][0] + zodziai2[1][0] + zodziai2[2][0]
print(akronimas2)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(tekstas2.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(tekstas2.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
tekstas3 = 'Coding For All People'
print(tekstas3.rfind('I'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sakinys4 = 'You cannot end a sentence with because because because is a conjunction'
print(sakinys4.find('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sakinys4.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
pradzios_indeksas = sakinys4.find('because')
pabaigos_indeksas = sakinys4.rfind('because')
print(sakinys4[pradzios_indeksas:pabaigos_indeksas+7])

#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# kartojasi

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# kartojasi

#28 Does 'Coding For All' start with a substring Coding?
print(tekstas2.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
print(tekstas2.endswith('coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
tekstas4 = '   Coding For All      '
print(tekstas4.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
variable1 = '30DaysOfPython'
variable2 = 'thirty_days_of_python'
print(variable1.isidentifier())
print(variable2.isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(libraries))

#33 Use the new line escape sequence to separate the following sentences.
print('I am enjoying this challenge.\nI just wonder what is next.')

#34 Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

#35 Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2

print(f"The area of a circle with radius {radius} is {int(area)} meters square.")
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

#36 Make the following using string formatting methods:
"""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")  # :.2f palieka tik du skaičius po kablelio
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")