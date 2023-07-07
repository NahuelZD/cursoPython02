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