# collect input numbers from the user
# determine if the given number is even or odd
# Hint: if a number is divided by 2 and a reminder is 0 ,and it is greater than 0 we call that number even




num=int(input('Enter input number:'))
mod = num % 2
if mod == 0 and num >0:
    print('This is an even number.')
else:
    print('This is a odd number')


