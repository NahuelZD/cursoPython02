# High Order Functions
def increment(x):
    return x + 1

def high_order_func(x, func):
    return x + func(x)

result = high_order_func(3, increment)
print(result)

increment_v2 = lambda x : x + 1
high_order_func_v2 = lambda x, func : x + func(x)

result_v2 = high_order_func_v2(3, increment_v2)
print(result_v2)

result = high_order_func_v2(3, lambda x : x * 2)
print(result)
result = high_order_func_v2(3, lambda x : x + 5)
print(result)
result = high_order_func_v2(3, lambda x : x / 3)
print(result)