# Program to calculate the sum of digits of an integer

# Get input from user
num = int(input("Enter an integer: "))

# Make a copy to handle negative numbers
n = abs(num)

sum_of_digits = 0

# Loop to extract and sum digits
while n > 0:
    digit = n % 10          # Get the last digit
    sum_of_digits += digit  # Add it to the sum
    n //= 10                # Remove the last digit

print(f"The sum of digits of {num} is {sum_of_digits}")
