# Program to print a triangle of numbers from 1 to 5

for i in range(1, 6):        # Loop from 1 to 5
    for j in range(1, i + 1):  # Inner loop to print numbers in each row
        print(j, end=" ")      # Print numbers on the same line
    print()                    # Move to the next line
