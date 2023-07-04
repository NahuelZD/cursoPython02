numbers = []

for element in range(1, 11):
    numbers.append(element)
    
print(numbers)

numbersV2 = [element for element in range(1, 11)]
print(numbersV2)

# --------------------------------------------------------------------

duplicado = []

for element in range(1, 11):
    duplicado.append(element * 2)
    
print(duplicado)

duplicadoV2 = [element * 2 for element in range(1, 11)]
print(duplicadoV2)

# Aplicar condiciones
paridad = [i for i in range(1, 11) if i % 2 == 0]
print(paridad)