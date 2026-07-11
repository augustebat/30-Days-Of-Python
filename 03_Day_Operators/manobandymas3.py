# 1. Declare your age as integer variable
my_age = 21

# 2. Declare your height as a float variable
my_height = 1.71

# 3. Declare a variable that store a complex number
complex_num = 4 + 3j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = float(input("Iveskite trikampio pagrindo ilgi: "))
height = float(input("Iveskite trikampio auksti: "))
area = 0.5 * base * height
print("Trikampio plotas:", area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a= input("Iveskite krastine a: ")
side_b= input("Iveskite krastine a: ")
side_c= input("Iveskite krastine a: ")
perimeter = side_a + side_b + side_c
print("Trikampio perimetras", perimeter)

# 6. Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rec_length = int(input("Iveskite staciakampio ilgi"))
rec_width = int(input ("Iveskite staciakampio ploti"))
rec_area = rec_length * rec_width
print("Staciakampio plotas:", rec_area) 
print("Staciakampio perimetras:", 2*(rec_length+rec_width))

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Iveskite apskritimo spindulio ilgi:"))
pi = 3.14
circle_area = pi * (radius ** 2)
circle_circum = 2*pi*radius
print("Apskritimo plotas:",circle_area )
print("Apskritimo ilgis:",circle_circum)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
# y= mx+b = 2x -2
m = 2
b = -2
slope = m
y_intercept = b
# x-intercept 0 = mx + b -> mx = -b -> x = -b / m
x_intercept = -b / m
print(f"Nuolydis (Slope): {slope}")
print(f"y sankirta (y-intercept): {y_intercept} (taškas: (0, {y_intercept}))")
print(f"x sankirta (x-intercept): {x_intercept} (taškas: ({x_intercept}, 0))")

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1=2
y1=2
x2=6
y2=10
slope2 = (y2-y1)/(x2-x1)
euklidas = (((x2-x1)**2) + ((y2-y1)**2))**0.5
print("Antrasis nuolydis:", slope2)
print("Euklidas:", euklidas)

# 10. Compare the slopes in tasks 8 and 9.
print(slope == slope2)

# 11. Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at what x value y is going to be 0.
# x = -3
x = int(input("Iveskite x reiksme:"))
y = x**2 + 6*x + 9
print("lygties rezultatas: ", y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
pitono_ilgis = len('python')
drakono_ilgis = len('dragon')
print(pitono_ilgis != drakono_ilgis)

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sakinys = 'I hope this course is not full of jargon'
print('jargon' in sakinys)

# 15. There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

# 16. Find the length of the text python and convert the value to float and convert it to string
zodis = 'python'
zodzio_ilgis = len(zodis)
print("Zodzio python ilgis: ", zodzio_ilgis)
zodis2=float(zodzio_ilgis)
print("Reiksme paversta i float ", zodis2)
zodis3=str(zodzio_ilgis)
print("Reiksme paversta i string ", zodis3)

# 17. Even numbers are divisible by 2 and the remainder is zero. 
# How do you check if a number is even or not using python?
skaicius = int(input("Iveskite skaiciu:"))
print(skaicius % 2 == 0)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
rezultatas = 7//3
print(rezultatas == int(2.7))

# 19. Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Iveskite darbo valandu kieki: "))
rate_per_hour = int(input("Iveskite valandini uzmokesti: "))
earning = hours * rate_per_hour
print("Visas atlyginimas: ", earning)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Iveskite kiek metu nugyvenote:" ))
sekundes = years * 365 * 24 * 60 * 60
print(f"Gyvenate {sekundes} sekundziu.")

# 23. Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
print("1 1 1 1 1")
print(f"2 1 2 {2**2} {2**3}")
print(f"3 1 3 {3**2} {3**3}")
print(f"4 1 4 {4**2} {4**3}")
print(f"5 1 5 {5**2} {5**3}")



 