# Day 2: 30 Days of python programming
first_name = 'Augustė'
last_name = 'Bataitytė'
full_name = 'Augustė Bataitytė'
country = 'Lithuania'
city = 'Kaunas'
age = 21
year = 2026
is_married = False
is_true = True
is_light_on = True
favorite_color, favorite_food, dog_name = 'Blue', 'Pizza', 'Luna' 

print(type(first_name))  
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(favorite_color))
print(type(favorite_food))
print(type(dog_name))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = input("Enter radius of a circle: ")
area_of_circle = 3.14 * int(radius) ** 2
circum_of_circle = 2 * 3.14 * int(radius)
print("Area of circle:", area_of_circle)
print("Circumference of circle:", circum_of_circle)

vardas = input("Iveskite savo varda: ")
print("Jusu vardas:", vardas)
pavarde = input("Iveskite savo pavarde: ")
print("Jusu pavarde:", pavarde)
salis = input("Iveskite savo gimtaja sali:")
print("jusu gimtoji salis:", salis)
amzius = input("Iveskite savo amziu:")
print("Jusu amzius:", amzius)

print("Jusu ivesta informacija: ", vardas, pavarde,salis, amzius)