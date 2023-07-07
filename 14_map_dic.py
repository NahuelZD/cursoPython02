items = [
    {
        'product': 'camisa',
        'price': 100
    },
    
    {
        'product': 'pantalones',
        'price': 200
    },
    
    {
        'product': 'gorra',
        'price': 50
    }
]

prices = list(map(lambda item : item['price'], items))
print(prices)

# Agregar un atributo al dicc
def add_taxes(item):
    item['taxes'] = item['price'] * .21
    return item

new_items = list(map(add_taxes, items))
print(items)

# Esto anterior me modifica el array original
# Para eso, tenemos que crear una copia del diccionario anterio

'''
def add_taxes(item):
    new_item = item.copy.()
    new_item['taxes'] = new_item['price'] * .21
    return new_item
'''