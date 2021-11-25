cities = ['new York', 'lagos', 'abuja', 'Port harcourt']
capitalized_cites = []
for city in cities:
    capitalized_cites.append(city.title())
print(capitalized_cites)


#Shorted Method
capitalized_cites = [city.title() for city in cities]
print(capitalized_cites)

sqaure = [ x**2 for x in range(9) if x % 2 == 0]
print(sqaure)


names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = [name.split()[0].lower() for name in names]
print(first_names)



string_list = ["a", "B", "C"]

string_list = [each_string.lower() for each_string in string_list[0]]
print(string_list)

indices = [i for i, x in enumerate(names) if x == "whatever"]
print(indices)