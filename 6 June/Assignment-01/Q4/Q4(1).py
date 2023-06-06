import random
import string

for _ in range(100):
    length = random.randint(6, 8)
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
    print(random_string)
