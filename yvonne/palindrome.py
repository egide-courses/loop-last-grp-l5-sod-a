# Ask the user to enter a string
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate comparison
clean_text = text.replace(" ", "").lower()

# Use a loop to check if it's a palindrome
is_palindrome = True
length = len(clean_text)

for i in range(length // 2):
    if clean_text[i] != clean_text[length - i - 1]:
        is_palindrome = False
        break

# Display the result
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
