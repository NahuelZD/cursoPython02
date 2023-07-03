'''
CONJUNTOS:
-> SE PUEDEN MODIFICAR
-> NO TIENEN UN ORDEN
-> NO PERMITEN DUPLICADOS
'''

set_countries = {
    'col',
    'mex',
    'bol'
}

# Si repito algún elemento, directamente lo elimina al duplicado

print(set_countries)
print(type(set_countries))

set_numbers_ = {
    1,
    2,
    3,
    3,
    443,
    23
}

print(set_numbers_)
print(type(set_numbers_))

# Set a partir de un string
set_from_string = set('hola')
print(set_from_string)

# Set a partir de tuplas
set_from_tuple = set(('abc', 'Nahuel', 'Lola', 'abc'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
uniqueNumbers = list(set_numbers)
print(uniqueNumbers)