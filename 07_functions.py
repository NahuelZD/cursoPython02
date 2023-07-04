import random

# Funciones
def myPrint():
    print('Esta es mi primera función.')
    print('Este es el segundo print.')

myPrint()

# Definición con parámetro
def suma(a, b):
    print(a + b)

for i in range(1, 5):
    suma(random.randint(1, 100), random.randint(1, 100))