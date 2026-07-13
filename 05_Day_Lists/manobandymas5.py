#1 Declare an empty list
list = []

#2 Declare a list with more than 5 items
komandos = ['Zalgiris', 'Rytas', 'Lietkabelis', 'Neptunas', 'Juventus', 'Nevezis']
print(komandos)

#3 Find the length of your list
masyvo_ilgis = len(komandos)
print(f'Masyvo ilgis: {masyvo_ilgis}')

#4 Get the first item, the middle item and the last item of the list
paskutinis = masyvo_ilgis -1
vidurys =int(masyvo_ilgis/2)
print(f'Pirmas objektas{komandos[0]} \nVidurinis objektas:{komandos[vidurys]}, \nPaskutinis objektas:{komandos[paskutinis]}')

#5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Auguste', 21, 1.71, False, 'Kaunas']

#6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
companies = len(it_companies)
print(f'number of companies: {companies}')

#9 Print the first, middle and last company
last_index = companies -1
middle =int(companies/2)
print(f'Pirma: {it_companies[0]}, vidurine:{it_companies[middle]}, paskutine: {it_companies[last_index]}')

#10 Print the list after modifying one of the companies
it_companies[0] = 'NordSecurity'
print(it_companies)

#11 Add an IT company to it_companies
it_companies.append('Centric IT Solutions')
print(it_companies)