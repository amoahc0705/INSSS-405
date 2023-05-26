def get_numbers(num_count):
    numbers = []
    for i in range(num_count):
        number = float(input("Enter number {}: ".format(i+1)))
        numbers.append(number)
    return numbers
def calculate_mean(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    return mean
def calculate_sum(numbers):
    return sum(numbers)
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(numbers)
    if length % 2 == 0:
        mid1 = sorted_numbers[length // 2]
        mid2 = sorted_numbers[length // 2 - 1]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_numbers[length // 2]
    return median

# Collecting input number
num_count = 10
input_numbers = get_numbers(num_count)

# Calculating mean
mean = calculate_mean(input_numbers)

# Calculating sum
sum_result = calculate_sum(input_numbers)

#Calculating median
median = calculate_median(input_numbers)

#Printing the results
print("Input number:", input_numbers)
print("Mean:", mean)
print("Sum:", sum_result)
print("Median:", median)







