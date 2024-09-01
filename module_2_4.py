numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print('numbers = ', numbers)
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
     if numbers[i] != 1:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
                break
        if is_prime == False:
            not_primes.append(numbers[i])
        elif is_prime == True:
            primes.append(numbers[i])
        is_prime = True
print(f'Primes: {primes} \nNot Primes: {not_primes}')