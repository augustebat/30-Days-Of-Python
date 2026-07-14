#-----------Level 1-----------

#1 Create an empty tuple
tpl1=()

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Emma', 'Lucy', 'Trinity')
brothers = ('Zach', 'Bryce')

#3 Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#4 How many siblings do you have?
print(f'I have {len(siblings)} siblings')

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Melanie', 'Caleb')
print('My family: ', family_members)



#-----------Level 2-----------

#1 Unpack siblings and parents from family_members


#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Banana', 'Apple', 'Orange')
vegetables = ('Carrot', 'Tomato', 'Onion')
animal_products = ('Meat', 'Eggs', 'Honey')
food_stuff_tp = fruits+vegetables+animal_products
print()
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_count = len(food_stuff_lt) - 1
middle = int(food_count / 2)
print(f'Middle item: {food_stuff_lt[middle]}')

#5 Slice out the first three items and the last three items from food_stuff_lt list
print(f'First 3 items: {food_stuff_lt[0:3]}')
print(f'Last 3 items: {food_stuff_lt[-3:]}')

#6 Delete the food_stuff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries)