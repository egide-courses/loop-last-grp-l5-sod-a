# Display all prime numbers between 1 and 100

for num in range(2, 101):  # start from 2, since 1 is not prime
    is_prime = True  # assume the number is prime
    
    for i in range(2, int(num**0.5) + 1):  # check divisors up to the square root
        if num % i == 0:
            is_prime = False
            break  # not a prime number, exit inner loop
    
    if is_prime:
        print(num)
