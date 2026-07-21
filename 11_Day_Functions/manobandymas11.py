import math
#-----------Level 1-----------

#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    sum = a+b
    return sum

print(add_two_numbers(5, 3))


#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(pi, r):
    area = pi*r*r
    return area

print(area_of_circle(3.14, 3))


#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    suma = 0
    for num in nums:
        if isinstance(num, (int, float)):
            suma += num
        else:
            return "Visi argumentai turi būti skaičiai!"
    return suma

print(add_all_nums(1,2,3,4,5,6))

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fah = (celsius*(9/5) + 32)
    return fah

print(convert_celsius_to_fahrenheit(24))


#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Neteisingai įvestas mėnuo!"
    
your_month = str(input("Enter a month:")).lower()
print(check_season(your_month))

#6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "vertikali linija"
    slope = (y2 - y1) / (x2 - x1)
    return slope

rezultatas = calculate_slope(1, 2, 3, 6)
print(f"Nuolydis m = {rezultatas}")  


#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Du sprendiniai: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Vienas sprendinys: x = {x}"
    else:
        return "Realių sprendinių nėra"

print(solve_quadratic_eqn(1, -3, 2))  

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for x in lst:
        print(x)

lst = ['a', 'b', 'c']
print_list(lst)


#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
"""
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
"""
def reverse_list(sarasas):
    naujas_sarasas = []
    for x in sarasas:
        naujas_sarasas.insert(0, x)
    return naujas_sarasas

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"])) 
#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(sarasas):
    naujas_sarasas=[]
    for x in sarasas:
        naujas_sarasas.append(x.capitalize())
    return naujas_sarasas

fruits = ["apple", "banana", "cherry"]
print(capitalize_list_items(fruits))

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
"""
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]
"""
def add_item(lst, item):
    lst.append(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      

#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
"""
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
"""
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_stuff2 = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff2, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers2 = [2, 3, 7, 9]
print(remove_item(numbers2, 3))  # [2, 7, 9]

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
"""
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
"""
def sum_of_numbers(num):
    suma = 0
    for i in range(num, 0,-1):
        suma+=i
    return suma

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    suma = 0
    for i in range(1, num+1):
        if i % 2 !=0:
            suma+=i
    return suma

print(sum_of_odds(5))  
print(sum_of_odds(10)) 
print(sum_of_odds(100)) 

#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    suma = 0
    for i in range(1, num+1):
        if i % 2 ==0:
            suma+=i
    return suma

print(sum_of_even(5))  
print(sum_of_even(10)) 
print(sum_of_even(100)) 
