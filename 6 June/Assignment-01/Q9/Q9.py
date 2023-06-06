import random
import string


random_strings = [''.join(random.choices(string.ascii_lowercase, k=random.randint(10, 15))) for _ in range(100)]


with open("random_strings.txt", "w") as file:
    
    for string in random_strings:
        file.write(string + "\n")
