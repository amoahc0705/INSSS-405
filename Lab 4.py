sum = 0.00
for i in range(9):
    score = input('Enter Score')
    sum = sum + int(score)
print("Sum:", sum)
average=int(sum)/9
print('final average', average)