def suma_with_range(a):
    sum = 0
    for x in range(1, a):
        sum += x
        print(sum)
    return sum
    
rango = int(input('Sumar hasta el número: '))

print(suma_with_range(rango))