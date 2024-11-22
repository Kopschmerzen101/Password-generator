import random  # Importing the random module to generate random samples

#Putting in the character sets
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # All uppercase letters
lowercase_letters = uppercase_letters.lower()  # All lowercase letters
digits = "0123456789"  # All digit characters
symbols = "(){}[],./';[]#$%"  # Some common symbols for password variety

# Options to include specific types of characters in the password
upper, lower, nums, syms = True, True, True, False  # To toggle between each character type

# Placing an empty string to hold the combined characters
all = ""

# Conditionally add character sets to the 'all' string based on selected options
if upper:
    all += uppercase_letters  # Add uppercase letters if upper is True
if lower:
    all += lowercase_letters  # Add lowercase letters if lower is True
if nums:
    all += digits  # Add digits if nums is True
if syms: 
    all += symbols  # Add symbols if syms is True

# These are the password parameters
length = 15  # Length of each password
amount = 20  # Number of passwords to generate

# Generate and print the specified number of passwords
for x in range(amount):
    # Create a password by randomly sampling 'length' characters from 'all'
    password = "".join(random.sample(all, length))
    print(password)  # Print each generated password
