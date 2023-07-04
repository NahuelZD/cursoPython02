# Importar
import math

# Definición de funciones
def volumen(area, h):
    return round(area * h)

def esfera(r):
    return round((4/3) * math.pi * r * r * r, 2)

def cono(area, h):
    return round(area * h / 3, 2)

def superficie_circulo(r):
    return round(math.pi * r * r, 2)

def superficie_triangulo(b, h):
    return round(b * h / 2, 2)

def superficie_cuadrilateros(b, h):
    return round(b * h, 2)

# ----------------------------------------------------------------------

# Ingresar la opción del cuerpo que se desea calcular
# ----------------------------------------------------------------------
print('[1] Esfera\n[2] Cono\n[3] Cubo\n[4] Prisma\n[5] Pirámide\n[6] Cilindro')

start = int(input('Selecciona el número del cuerpo a calcular el volúmen: '))
# ----------------------------------------------------------------------

# Lógica de la calculadora
# ----------------------------------------------------------------------
if start in (1, 2, 3, 4, 5, 6):
    if start == 1:
        radio = int(input('Ingresar el valor del rádio de la esfera: '))
        print(f"El volúmen de la esfera de radio {radio} cm es: {esfera(radio)} cm3")
    elif start == 2:
        radio = int(input('Ingresar el valor del rádio de la base del cono: '))
        altura = int(input('Ingresar el valor de la altura del cono: '))
        sup = superficie_circulo(radio)
        print(f"El volúmen del cono con radio {radio} cm y al altura {altura} cm es: {cono(sup, altura)} cm3")
    elif start == 3:
        lado = int(input('Ingresar el valor del lado del cubo: '))
        sup = superficie_cuadrilateros(lado, lado)
        print(f"El volúmen del cubo de lado {lado} cm es: {volumen(sup, lado)} cm3")
    elif start == 4:
        base = int(input('Ingresar el valor de la base de de la base del prisma: '))
        altura = int(input('Ingresar el valor de la altura de la base del prisma: '))
        altura_cuerpo = int(input('Ingresar el valor de la altura del cuerpo: '))
        sup = superficie_cuadrilateros(base, altura)
        print(f"El volúmen del prisma de base {base} cm y altura de la base {altura} cm es: {volumen(sup, altura_cuerpo)} cm3")
    elif start == 5:
        base = int(input('Ingresar el valor de la base de la base de la pirámide: '))
        altura = int(input('Ingresar el valor de la altura de la base de la pirámide: '))
        altura_cuerpo = int(input('Ingresar el valor de la altura de la pirámide: '))
        sup = superficie_cuadrilateros(base, altura)
        print(f"El volúmen de la pirámide de base {base} cm, altura de la base {altura} y altura {altura_cuerpo} cm es: {cono(sup, altura_cuerpo)} cm3")
    else:
        radio = int(input('Ingresar el valor del radio de la base del cilindro: '))
        altura = int(input('Ingresar el valor de la altura del cilindro: '))
        sup = superficie_circulo(radio)
        print(f"El volúmen del cilindro de radio {radio} cm y altura {altura} cm es: {volumen(sup, altura)} cm3")
else:
    print('Esa opción no está definida')