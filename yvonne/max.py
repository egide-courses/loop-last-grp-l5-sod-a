# Initialize variables
max_num = None
min_num = None

# Loop to take 10 numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))

    # For the first number, set both max and min
    if i == 0:
        max_num = num
        min_num = num
    else:
        # Update max and min as needed
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

# Display the results
print(f"\nMaximum value: {max_num}")
print(f"Minimum value: {min_num}")
