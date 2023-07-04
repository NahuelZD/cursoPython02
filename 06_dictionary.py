import random

# Ejemplo de YouTube
'''
dictionary = {key: expression for (key, value) in iterable}
dictionary = {key: expression for (key, value) in iterable if conditional}
'''
# -------------------------------------------------------------------------
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -------------------------------------------------------------------------


cities_in_Far = {
    'New York': 32,
    'Boston':75,
    'Los Ángeles': 100,
    'Chicago': 75
}

cities_in_Cel = {key: round((value-32) / 1.8) for (key, value) in cities_in_Far.items()}
print(cities_in_Far)
print(cities_in_Cel)
print('*' * 20)
print(cities_in_Cel.keys())
print(cities_in_Cel.values())
print(cities_in_Cel.items())
print('*' * 20)
# -----------------------------------------------------------------------------

countries = ['col', 'mex', 'bol', 'pe']

# {Que el pais: Tenga un numero random para cada pais (elemento) en la lista de paises}
population = {country: random.randint(1, 100) for country in countries}
print(population)

result = {country: popu for (country, popu) in population.items() if popu > 50}
print(result)

# -----------------------------------------------------------------------------
text = 'Hola, soy Nahuel'
unique = {caracter: caracter.upper() for caracter in text if caracter in 'aeiou'}
labels = {caracter: text.count(caracter) for caracter in text if caracter in 'aeiou'}
print(unique)
print(labels)