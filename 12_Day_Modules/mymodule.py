import random
import string

def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname

def sum_two_nums (num1, num2):
    return num1 + num2
gravity = 9.81
person = {
    "firstname": "Asabeneh",
    "age": 250,
    "country": "Finland",
    "city":'Helsinki'
}

#-----------Level 1-----------
#1 Write a function which generates a six digit/character random_user_id.
def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id

#2 Modify the previous task. 
# Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    num_of_characters = int(input('Enter the number of characters: '))
    num_of_ids = int(input('Enter the number of IDs to generate: '))
    characters = string.ascii_letters + string.digits

    ids = []
    for i in range(0, num_of_ids):
        ids.append(''.join(random.choices(characters, k=num_of_characters)))
    return '\n'.join(ids)


#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

#-----------Level 2-----------
#4 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    characters = string.hexdigits.lower()
    hex_codes = []
    for _ in range(num):
        hexa = ''.join(random.choices(characters, k=6))
        code = '#' + hexa
        hex_codes.append(code)
    return hex_codes

#5 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    rgb_codes = []
    for _ in range(num):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        coder = f"rgb({r}, {g}, {b})"
        rgb_codes.append(coder)
    return rgb_codes


#6 Write a function generate_colors which can generate any number of hexa or rgb colors.
"""
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
"""
    
def generate_colors(type, num):
    if type == 'hexa':
        return list_of_hexa_colors(num)
    elif type == 'rgb':
        return list_of_rgb_colors(num)
    else:
        return "Neteisingas tipas! Naudokite 'hexa' arba 'rgb'."
    

#-----------Level 3-----------
#7 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lst):
    if type(lst) is list:
        new_lst = random.shuffle(lst)
    return lst

#8 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random():
    return random.sample(range(10), k=7)