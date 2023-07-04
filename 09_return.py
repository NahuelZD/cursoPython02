import random

def find_volumen(b, h, w):
    return b * h * w
'''
def find_volumen(b = 1, h = 1, w = 1): Valores por defecto por si no le mando ningún valor o no le quieramos enviar alguno en específico
    return b * h * w , w , 'hola' -> Retorna una tupla con los valores (b*h*w, w, 'hola)
'''
for i in range(1, 5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    result = find_volumen(a, b, c)
    print(f"El volumen de la figura con base '{a} cm', altura de la base '{b} cm' y altura '{c} cm' es: {result} cm3")