import random

# Generate a list of 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

print("List of random numbers:", numbers)

# (i) 
odd_numbers = [num for num in numbers if num % 2 != 0]
count_odd = len(odd_numbers)
print("Odd numbers:", odd_numbers)
print("Count of odd numbers:", count_odd)

# (ii)
even_numbers = [num for num in numbers if num % 2 == 0]
count_even = len(even_numbers)
print("Even numbers:", even_numbers)
print("Count of even numbers:", count_even)

# (iii)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
count_prime = len(prime_numbers)
print("Prime numbers:", prime_numbers)
print("Count of prime numbers:", count_prime)
