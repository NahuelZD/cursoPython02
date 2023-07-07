price = 100 # Global

def increment():
    price = 200 # Local
    price += 10
    print(price)

print(price)
increment()