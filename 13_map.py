numbers = [1, 2, 3, 4, 5 , 6]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
    
print(numbers)
print(numbers_v2)

numbers_map = list(map(lambda element : element * 2, numbers))

print(numbers)
print(numbers_map)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]

result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(result)