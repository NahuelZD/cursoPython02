# print(0 / 0) # Error: Division by zero
# print(result) Error: 'result' is not defined

suma = lambda x, y : x + y
assert suma(2,2) == 4 # Resolver y verificar esta hipótesis
print('Hola 2')

age = 10
if age < 18:
    raise Exception('No se permiten menores de edad!') # Se lanza el error y ya no se ejecutan las instrucciones posteriores