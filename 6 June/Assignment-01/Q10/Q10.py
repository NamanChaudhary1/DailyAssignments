def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


with open("prime_numbers.txt", "w") as file:
    
    for num in range(600, 801):
        if is_prime(num):
            file.write(str(num) + "\n")
