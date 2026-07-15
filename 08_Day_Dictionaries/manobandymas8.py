#1 Create an empty dictionary called dog
dog = {}

#2 Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Luna', 'color':'black', 'breed':'daschund', 'legs':'short', 'age':'6'}
print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'Jonas',
    'last_name':'Jonaitis',
    'gender': 'male',
    'age':'21',
    'marital_status':'unmarried',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Lithuania',
    'city':'Vilnius',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}

#4 Get the length of the student dictionary
print(len(student))

#5 Get the value of skills and check the data type, it should be a list
skills_reiksme = student['skills']  
print(isinstance(skills_reiksme, list)) 
print(type(skills_reiksme)) 

#6 Modify the skills values by adding one or two skills
student['skills'].append('HTML')
print(student)

#7 Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)

#8 Get the dictionary values as a list
values_list = list(student.values())
print(values_list)

#9 Change the dictionary to a list of tuples using items() method
tuples = student.items()
print(tuples)

#10 Delete one of the items in the dictionary
student.popitem()
print(student)

student.pop('marital_status')
print(student)

#11 Delete one of the dictionaries
del dog