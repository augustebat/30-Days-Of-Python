from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g, random_user_id, user_id_gen_by_user, rgb_color_gen, list_of_hexa_colors, list_of_rgb_colors, generate_colors, shuffle_list as shuffle, seven_random

print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
print(mass)
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

#-----------Level 1-----------
#1 Write a function which generates a six digit/character random_user_id.
print(random_user_id()) 

#2 Modify the previous task. 
# Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print(user_id_gen_by_user()) # user input: 5 5
#print(user_id_gen_by_user()) # 16 5

#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# rgb(125,244,255) - the output should be in this form
print(rgb_color_gen())



#-----------Level 2-----------
#4 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array 
# (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print(list_of_hexa_colors(3))

#5 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print(list_of_rgb_colors(2))

#6 Write a function generate_colors which can generate any number of hexa or rgb colors.

print(generate_colors('hexa', 3)) # ['#a3e12f', '#03ed55', '#eb3d2b']
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175)', 'rgb(50, 105, 100)', 'rgb(15, 26, 80)']
print(generate_colors('rgb', 1))  # ['rgb(33, 79, 176)']



#-----------Level 3-----------
#7 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
names = ['Abigail', 'Bella', 'John', 'Mary']
print(shuffle(names))

#8 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print(seven_random())