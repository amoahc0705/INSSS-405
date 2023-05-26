import random

random_numbers = []  # Create an empty array to store the random integers
for _ in range (100): # Generate 100 random numbers and store them in array
    random_numbers.append(random.randint(1, 100))
odd_numbers = []     # Create an empty array to store the odd numbers

for num in random_numbers:  # Iterate over each number in the random_numbers array
    if num % 2 != 0:  # Check if the number is odd
        odd_numbers.append(num)  # If the number is odd, append it to the odd_numbers array

print("Odd numbers:")    # Print the odd numbers
for num in odd_numbers:
    print(num, end=" ")


