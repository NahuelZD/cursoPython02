for i in range(1, 12):
    print(i)
    
my_iterable = iter(range(1, 6))
print(my_iterable)
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable))
print(next(my_iterable)) # Límite, después da error