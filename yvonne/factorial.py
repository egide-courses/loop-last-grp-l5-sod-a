'''# Factorial using a for loop

# Get input from user
n = int(input("Enter a number: "))

factorial = 1

# Check if the number is valid
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is {factorial}")'''

    # Factorial using a while loop

n = int(input("Enter a number: "))

factorial = 1
i = 1

if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    while i <= n:
        factorial *= i
        i += 1
    print(f"The factorial of {n} is {factorial}")
