'''# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Skip numbers divisible by 3
    if i % 3 == 0:
        continue

    # Stop when number equals 73
    if i == 73:
        break

    # Print the number
    print(i)
'''

# Loop through numbers from 1 to 100
for i in range(1, 101):
    # Stop the loop when number equals 73
    if i == 73:
        break

    # Skip numbers divisible by 3
    if i % 3 == 0:
        continue

    # Print the current number
    print(i)
