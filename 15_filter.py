numbers = [1, 2, 3, 4, 5]
# Sólo la condición verdadera va a pertenecer a la nueva lista
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))

print('Antigua lista -> ', numbers)
# Crea una nueva lista, no modifica la antigua
print('Nueva lista -> ', new_numbers)