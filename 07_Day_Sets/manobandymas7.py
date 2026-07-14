#-----------Level 1-----------

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Find the length of the set it_companies
aibes_ilgis = len(it_companies)
print(it_companies)
print(f'\nlength of the set it_companies: {aibes_ilgis}')

#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('\nPrideta nauja kompanija:\n', it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_companies.update(['Nvidia','Tesla', 'Meta'])
print('\nPrideta nauju kompaniju:\n', it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print('\nSarasas po pasalinimo:\n', it_companies)

#5 What is the difference between remove and discard?
"""We can remove an item from a set using remove() method. 
If the item is not found remove() method will raise errors, 
so it is good to check if the item exist in the given set. 
However, discard() method doesn't raise any errors."""


#-----------Level 2-----------
#1 Join A and B
AB = A.union(B)
print()
print(AB)

#2 Find A intersection B
print(A.intersection(B))

#3 Is A subset of B
print(A.issubset(B))

#4 Are A and B disjoint sets
print(A.isdisjoint(B))

#5 Join A with B and B with A
print(A.union(B))  # Sujungia A su B
print(B.union(A))  # Sujungia B su A

#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7 Delete the sets completely
del A
del B



#-----------Level 3-----------

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
set_len = len(age_set)
lst_len = len(age)
print(f'List ilgis:{lst_len}, set ilgis: {set_len}')
print(set_len < lst_len)

#2 Explain the difference between the following data types: string, list, tuple and set
"""
string - Nekeičiamas (immutable), tvarkingas (ordered) simbolių rinkinys.
list - Keičiamas (mutable), tvarkingas elementų rinkinys. Leidžia dublikatus.
tuple - Nekeičiamas (immutable), tvarkingas rinkinys. Leidžia dublikatus.
set - Keičiamas, netvarkingas (unordered) rinkinys. Neleidžia jokių dublikatų.

"""
#3 I am a teacher and I love to inspire and teach people. 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
sakinys = 'I am a teacher and I love to inspire and teach people'
print(sakinys.lower())
zodziai = sakinys.split()
print(zodziai)
aibe = set(zodziai)
print(aibe)