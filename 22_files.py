file = open('./text.txt')
# print(file.read()) Leer todo el archivo
# print(file.readline()) Leer línea a línea

for line in file:
    print(line)

file.close() # Cierre del archivo

with open('./text.txt') as file: # Cierre de forma automática - Igual a lo anterior pero no hace falta poner el close
    for line in file:
        print(line)