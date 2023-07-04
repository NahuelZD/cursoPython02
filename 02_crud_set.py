set_countries = {
    'col',
    'mex',
    'bol'
}

# Cuantos elementos hay en el conjunto
size = len(set_countries)
print(size)

# Preguntar por el elemento
print('col' in set_countries)
print('pe' in set_countries)

# Agregar elementos
set_countries.add('pe')
print(set_countries)

# Actualizar un conjunto
set_countries.update({
    'arg',
    'ecu',
    'pe'
})
print(set_countries)

# Remover elementos del conjunto
set_countries.remove('col')
print(set_countries) # Si quiero remover un elemento que no existe da error

set_countries.discard('ecua') # No existe 'ecua', no lo encuentra, no da error
print(set_countries)

# Limpiar un conjunto
set_countries.clear()
print(set_countries)