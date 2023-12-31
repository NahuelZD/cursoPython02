'''
def increment(x):
    return x + 1

result = increment(10)
print(result)
'''

# Lambda func
result = lambda x : x + 1
print(result(20))

# .titlle() Primera letra mayúscula
full_name = lambda name, last_name : f"Full name is -> {name.title()} {last_name.title()}."

text = full_name('nahuel', 'zelaya')
print(text)

'''
¿Que es lambda?
Son conocidas como Funciones Anónimas o lambdas, en donde no tienen un identificador o no tienen un nombre, se puede definir su estructura de la siguiente manera: lambda argumentos: expresión, las funciones lambda pueden tener los argumentos que se requieran pero solo una linea de código o una expresión.

Sintaxis
lambda arguments : expression

Queremos incrementar el valor de una serie según la cantidad que le hayamos dado para ello tenemos el siguiente ejemplo:

def increment(x):
  return x + 1

increment_v2 = lambda x : x + 1

result = increment_v2(20)
print(result)

La función lambda puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión.


datos_completos = lambda name, last_name, age, countrie: f'Sus datos completos son {name.title()} {last_name.title()} tiene {age} años y vive en {countrie.title()}'
text = datos_completos('camilo', 'mejia', 35, 'colombia')
print(text)

'''