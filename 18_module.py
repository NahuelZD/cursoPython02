import sys # Sistema operativo
print(sys.path)

import re
text = 'Mi número de teléfono es 123 321 111, y el código del país es 57. Mi número de la suerte es 6.'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
local_time = time.asctime(local)
print(timestamp)
print(local_time)

import collections
numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 1, 2, 3, 4]
counter = collections.Counter(numbers)

print(counter)