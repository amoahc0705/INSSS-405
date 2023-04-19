# Ask a user to enter 10 numbers
# Determine if number is even or odd
for x in range(10):
    num = int(input('Enter a number: '))
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')


