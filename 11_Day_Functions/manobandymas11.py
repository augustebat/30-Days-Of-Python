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



#-----------Level 2-----------
#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):
    count_evens = 0
    count_odds = 0
    for i in range(0, number+1):
        if i % 2 == 0:
            count_evens += 1
        else:
            count_odds+=1
    return f"The number of odds are {count_odds}.\nThe number of evens are {count_evens}."

print(evens_and_odds(100))

#2 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    fakt = 1
    for i in range(1, number+1):
        fakt *= i
    return f'Skaiciaus {number} faktorialas yra: {fakt}'

print(factorial(5))

#3 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param=None):
    if not param:  # Jei 'param' yra tuščias (False)
        return True
    else:          # Jei 'param' turi reikšmę (True)
        return False

print(is_empty([]))        
print(is_empty(""))        
print(is_empty("Labas"))   
print(is_empty([1, 2, 3])) 


#4 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)

def calculate_median(lst):
    if not lst:
        return None
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    
    if n % 2 != 0:
        return sorted_lst[mid]
    else:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    
def calculate_mode(lst):
    if not lst:
        return None
    
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
        
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    
    if max_count == 1:
        return "Modos nėra (visi skaičiai unikalūs)"
    
    return modes if len(modes) > 1 else modes[0]

def calculate_range(lst):
    if not lst:
        return None
    return max(lst) - min(lst)

def calculate_variance(lst):
    if not lst or len(lst) < 2:
        return 0
    
    mean = calculate_mean(lst)
    variance = sum((x - mean) ** 2 for x in lst) / len(lst)
    return variance

def calculate_std(lst):
    if not lst:
        return None
    variance = calculate_variance(lst)
    return variance ** 0.5 

data = [4, 7, 3, 8, 1, 7, 9, 7, 2]
print(f"Duomenys: {data}")
print(f"Vidurkis (Mean): {calculate_mean(data):.2f}")
print(f"Mediana (Median): {calculate_median(data)}")
print(f"Moda (Mode): {calculate_mode(data)}")
print(f"Plotis (Range): {calculate_range(data)}")
print(f"Dispersija (Variance): {calculate_variance(data):.2f}")
print(f"Standartinis nuokrypis (Std Dev): {calculate_std(data):.2f}")

#5 Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
"""
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
"""
def greet(name = None):
    if not name:
        return "Hello, Guest!"
    else:
        return f'Hello, {name}'
    
print(greet())
print(greet('Alice'))

#6 Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
"""
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
"""
def show_args(**args):
    formatted_items = [f"{k}: {v}" for k, v in args.items()]
    print(f"Received: {', '.join(formatted_items)}")

show_args(name="Alice", age=30, city="New York") # Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny") # Received: name: Bob, pet: Fluffy, the bunny




#-----------Level 3-----------
#1 Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        
    return True

print(is_prime(1))   # False
print(is_prime(2))   # True
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(13))  # True

#2 Write a functions which checks if all items are unique in the list.
def check_unique(lst):
    return len(lst) == len(set(lst))

print(check_unique([1, 2, 3, 4, 5]))  
print(check_unique([1, 2, 2, 4, 5]))  

#3 Write a function which checks if all the items of the list are of the same data type.
def check_same_type(lst):
    if not lst:
        return True 
    first_type = type(lst[0])
    for item in lst:
        if type(item) != first_type:
            return False
            
    return True

print(check_same_type([1, 2, 3, 4]))       
print(check_same_type(['a', 'b', 'c']))     
print(check_same_type([1, '2', 3, 4]))       

#4 Write a function which check if provided variable is a valid python variable
import keyword
def is_valid_variable(var_name):
    if isinstance(var_name, str) and var_name.isidentifier() and not keyword.iskeyword(var_name):
        return True
    return False

print(is_valid_variable("my_variable"))  
print(is_valid_variable("var123"))       
print(is_valid_variable("123var"))       
print(is_valid_variable("my-var"))       
print(is_valid_variable("def"))         