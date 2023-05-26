import random

# Generate 100 random numbers
random_numbers = [random.randint(1, 1000) for _ in range(100)]

# Sort the random numbers
def sort_numbers(numbers):
    sorted_numbers = numbers.copy()
    sorted_numbers.sort()
    return sort_numbers
sorted_numbers = sort_numbers(random_numbers)

# Print the sorted numbers
print("Original numbers:")
print(random_numbers)
print("\nSorted numbers:")
print(sorted_numbers)

