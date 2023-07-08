import utils

keys, values = utils.get_population()
print(keys, values)

text = utils.A
print(text)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Bolivia',
        'Population': 500
    }
]

result = utils.population_by_country(data, 'Bolivia')
print(result)